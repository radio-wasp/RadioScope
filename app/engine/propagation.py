import math
from typing import List, Dict, Tuple, Any
from app.models import Station, ContourTier, RadialProfilePoint, SignalProbeResponse
from app.engine.geodesy import (
    calculate_distance_bearing,
    generate_polygon_coordinates,
    calculate_polygon_area_sqkm
)

# Standard FM Contour Tiers (dBu)
FM_CONTOURS = [
    {
        "level_dbu": 70.0,
        "name": "City Grade (70 dBu / 3.16 mV/m)",
        "description": "Strong, pristine indoor and mobile stereo reception. Solid building penetration.",
        "color": "#10b981",  # Emerald
        "stroke_color": "#059669",
        "fill_opacity": 0.35,
    },
    {
        "level_dbu": 60.0,
        "name": "Protected Service (60 dBu / 1.00 mV/m)",
        "description": "Standard licensed coverage area. Clear car stereo and home antenna reception.",
        "color": "#3b82f6",  # Blue
        "stroke_color": "#2563eb",
        "fill_opacity": 0.25,
    },
    {
        "level_dbu": 54.0,
        "name": "Secondary / Suburban (54 dBu / 0.50 mV/m)",
        "description": "Moderate signal. Good car radio reception; may experience light noise indoors.",
        "color": "#f59e0b",  # Amber
        "stroke_color": "#d97706",
        "fill_opacity": 0.18,
    },
    {
        "level_dbu": 48.0,
        "name": "Fringe / DX (48 dBu / 0.25 mV/m)",
        "description": "Weak signal boundary. Sensitive car tuner or outdoor high-gain antenna required.",
        "color": "#8b5cf6",  # Purple
        "stroke_color": "#7c3aed",
        "fill_opacity": 0.12,
    },
]

# Standard AM Contour Tiers (mV/m and equivalent dBu)
AM_CONTOURS = [
    {
        "level_mvm": 25.0,
        "level_dbu": 88.0,
        "name": "Business / City Core (25 mV/m)",
        "description": "High signal strength overcoming heavy urban electromagnetic interference.",
        "color": "#10b981",
        "stroke_color": "#059669",
        "fill_opacity": 0.35,
    },
    {
        "level_mvm": 5.0,
        "level_dbu": 74.0,
        "name": "Residential / City Grade (5 mV/m)",
        "description": "Solid residential coverage with low background noise.",
        "color": "#3b82f6",
        "stroke_color": "#2563eb",
        "fill_opacity": 0.25,
    },
    {
        "level_mvm": 2.0,
        "level_dbu": 66.0,
        "name": "Primary Service Area (2 mV/m)",
        "description": "Standard daytime protected primary service boundary.",
        "color": "#f59e0b",
        "stroke_color": "#d97706",
        "fill_opacity": 0.18,
    },
    {
        "level_mvm": 0.5,
        "level_dbu": 54.0,
        "name": "Rural Protected Contour (0.5 mV/m)",
        "description": "Official rural daytime coverage contour boundary.",
        "color": "#8b5cf6",
        "stroke_color": "#7c3aed",
        "fill_opacity": 0.12,
    },
]


def dbu_to_mvm(dbu: float) -> float:
    """Convert field strength from dBu (dB referenced to 1 uV/m) to mV/m."""
    return round(10.0 ** ((dbu - 60.0) / 20.0), 3)


def mvm_to_dbu(mvm: float) -> float:
    """Convert field strength from mV/m to dBu."""
    if mvm <= 0:
        return 0.0
    return round(20.0 * math.log10(mvm) + 60.0, 1)


# =========================================================================
# FCC F(50,50) FM Propagation Model (47 CFR § 73.313 / § 73.333 & ITU-R P.1546)
# =========================================================================

def calculate_fm_f50_50_field_strength(distance_km: float, haat_m: float, erp_kw: float) -> float:
    """
    Calculate predicted FM field strength in dBu at a given distance (km),
    given Height Above Average Terrain (HAAT in meters) and ERP (kW).
    Follows FCC 47 CFR § 73.333 curves and ITU-R P.1546.
    """
    if distance_km <= 0.1:
        distance_km = 0.1
    haat = max(10.0, min(1600.0, haat_m))
    erp = max(0.001, erp_kw)

    # Effective radio line of sight distance (4/3 earth radius model)
    d_los = 4.124 * (math.sqrt(haat) + math.sqrt(2.0))

    # Free-space field strength at 1 km for 1 kW is approx 106.9 dBu
    # ERP adjustment in dBk
    erp_dbk = 10.0 * math.log10(erp)

    # Standard FCC F(50,50) curve empirical parametric model:
    # 1. Height gain factor
    height_gain = 20.0 * math.log10(haat / 100.0)

    # 2. Distance attenuation
    if distance_km <= d_los:
        # Near/line-of-sight region: standard 2-ray & diffraction loss
        # Gradual transition from free-space (20*log) to ground reflection (40*log)
        ratio = distance_km / max(1.0, d_los)
        attenuation_exponent = 20.0 + 15.0 * (ratio ** 1.5)
        path_loss = attenuation_exponent * math.log10(distance_km)
    else:
        # Beyond line of sight (diffraction & tropospheric scatter)
        los_loss = 35.0 * math.log10(d_los)
        scatter_loss = 48.0 * math.log10(distance_km / d_los)
        path_loss = los_loss + scatter_loss

    f_1kw = 106.92 + height_gain - path_loss - 2.5
    e_field = f_1kw + erp_dbk

    return max(0.0, min(140.0, e_field))


def solve_fm_contour_distance_km(target_dbu: float, haat_m: float, erp_kw: float) -> float:
    """
    Solve for the distance in km where the predicted field strength equals target_dbu
    using bisection numerical solver.
    """
    d_min = 0.5
    d_max = 250.0

    # Test endpoints
    e_min = calculate_fm_f50_50_field_strength(d_min, haat_m, erp_kw)
    if target_dbu >= e_min:
        return d_min

    e_max = calculate_fm_f50_50_field_strength(d_max, haat_m, erp_kw)
    if target_dbu <= e_max:
        return d_max

    # Binary search convergence
    for _ in range(30):
        d_mid = (d_min + d_max) / 2.0
        e_mid = calculate_fm_f50_50_field_strength(d_mid, haat_m, erp_kw)

        if abs(e_mid - target_dbu) < 0.05:
            return round(d_mid, 2)

        if e_mid > target_dbu:
            d_min = d_mid
        else:
            d_max = d_mid

    return round((d_min + d_max) / 2.0, 2)


# =========================================================================
# AM Groundwave Propagation Model (FCC 47 CFR § 73.183 / § 73.184)
# =========================================================================

def calculate_am_groundwave_field_strength(
    distance_km: float,
    power_kw: float,
    freq_khz: float,
    conductivity_ms: float = 8.0
) -> Tuple[float, float]:
    """
    Calculate AM daytime groundwave field strength in mV/m and dBu
    using Sommerfeld-Norton groundwave formula with spherical earth attenuation.
    """
    if distance_km <= 0.1:
        distance_km = 0.1
    p_kw = max(0.1, power_kw)
    freq_mhz = freq_khz / 1000.0
    sigma = max(0.5, conductivity_ms)

    # Unattenuated field at 1 km (standard ~300 to 380 mV/m per sqrt(kW))
    e0_mvm = 350.0 * math.sqrt(p_kw)

    # Numerical distance p (Sommerfeld)
    # p ≈ (0.00844 * d_km * f_mhz^2) / sigma
    p = (0.00844 * distance_km * (freq_mhz ** 2)) / sigma

    # Norton attenuation factor A(p)
    # Empirical rational approximation to Sommerfeld attenuation function:
    a_p = (2.0 + 0.3 * p) / (2.0 + p + 0.6 * (p ** 2))

    # Curved earth diffraction correction
    curvature_loss = math.exp(-0.012 * (freq_mhz ** (1.0 / 3.0)) * distance_km)
    a_factor = a_p * curvature_loss

    e_mvm = (e0_mvm / distance_km) * a_factor
    e_dbu = mvm_to_dbu(e_mvm)

    return e_mvm, e_dbu


def solve_am_contour_distance_km(
    target_mvm: float,
    power_kw: float,
    freq_khz: float,
    conductivity_ms: float = 8.0
) -> float:
    """
    Solve for distance in km where AM daytime groundwave field equals target_mvm.
    """
    d_min = 0.5
    d_max = 400.0

    for _ in range(30):
        d_mid = (d_min + d_max) / 2.0
        e_mvm, _ = calculate_am_groundwave_field_strength(d_mid, power_kw, freq_khz, conductivity_ms)

        if abs(e_mvm - target_mvm) < 0.01:
            return round(d_mid, 2)

        if e_mvm > target_mvm:
            d_min = d_mid
        else:
            d_max = d_mid

    return round((d_min + d_max) / 2.0, 2)


# =========================================================================
# Radial Pattern & Antenna Directionality
# =========================================================================

def get_azimuth_power_multiplier(
    azimuth_deg: float,
    directional: bool = False,
    beam_heading_deg: float = 0.0
) -> float:
    """
    Returns power multiplier (0.05 to 1.0) along a given bearing.
    For omnidirectional, returns 1.0.
    For directional, applies cardioid/elliptical directional pattern centered on beam_heading_deg.
    """
    if not directional:
        return 1.0

    # Directional cardioid pattern with 15dB front-to-back ratio
    angle_diff = math.radians(azimuth_deg - beam_heading_deg)
    # Normalized field: 0.5 * (1 + cos(angle_diff))
    relative_field = 0.2 + 0.8 * (0.5 * (1.0 + math.cos(angle_diff)))
    power_mult = relative_field ** 2
    return max(0.04, min(1.0, power_mult))


# =========================================================================
# Contour Generation Pipeline
# =========================================================================

def generate_station_contours(station: Station) -> Tuple[List[ContourTier], Dict[str, Any], List[RadialProfilePoint]]:
    """
    Generate multi-tier coverage contours, GeoJSON FeatureCollection, and radial profile.
    """
    is_am = station.band.upper() == "AM"
    tiers_config = AM_CONTOURS if is_am else FM_CONTOURS
    calculated_tiers: List[ContourTier] = []
    features: List[Dict[str, Any]] = []

    # 360 radials (1 deg resolution)
    num_radials = 360

    for tier_info in tiers_config:
        radial_distances: List[float] = []

        for azimuth in range(num_radials):
            power_mult = get_azimuth_power_multiplier(
                azimuth,
                directional=station.directional,
                beam_heading_deg=0.0
            )
            effective_erp = station.erp_kw * power_mult

            if is_am:
                target_mvm = tier_info["level_mvm"]
                dist = solve_am_contour_distance_km(
                    target_mvm=target_mvm,
                    power_kw=effective_erp,
                    freq_khz=station.frequency,
                    conductivity_ms=8.0
                )
            else:
                target_dbu = tier_info["level_dbu"]
                dist = solve_fm_contour_distance_km(
                    target_dbu=target_dbu,
                    haat_m=station.haat_m,
                    erp_kw=effective_erp
                )
            radial_distances.append(dist)

        coords_ring = generate_polygon_coordinates(
            station.latitude,
            station.longitude,
            radial_distances
        )
        area_sqkm = calculate_polygon_area_sqkm(coords_ring)
        area_sqmi = round(area_sqkm * 0.386102, 1)
        avg_radius = round(sum(radial_distances) / len(radial_distances), 1)
        max_radius = round(max(radial_distances), 1)

        level_dbu = tier_info["level_dbu"]
        level_mvm = tier_info.get("level_mvm", dbu_to_mvm(level_dbu))

        geometry_polygon = {
            "type": "Polygon",
            "coordinates": [coords_ring]
        }

        tier_obj = ContourTier(
            level_dbu=level_dbu,
            level_mvm=level_mvm,
            name=tier_info["name"],
            description=tier_info["description"],
            color=tier_info["color"],
            stroke_color=tier_info["stroke_color"],
            fill_opacity=tier_info["fill_opacity"],
            avg_radius_km=avg_radius,
            max_radius_km=max_radius,
            area_sqkm=area_sqkm,
            area_sqmi=area_sqmi,
            geometry=geometry_polygon
        )
        calculated_tiers.append(tier_obj)

        # Build GeoJSON Feature for this contour
        features.append({
            "type": "Feature",
            "properties": {
                "callsign": station.callsign,
                "tier_name": tier_info["name"],
                "level_dbu": level_dbu,
                "level_mvm": level_mvm,
                "avg_radius_km": avg_radius,
                "area_sqkm": area_sqkm,
                "area_sqmi": area_sqmi,
                "color": tier_info["color"],
                "stroke_color": tier_info["stroke_color"],
                "fill_opacity": tier_info["fill_opacity"],
                "description": tier_info["description"]
            },
            "geometry": geometry_polygon
        })

    # Add Transmitter Point Feature
    features.append({
        "type": "Feature",
        "properties": {
            "type": "transmitter",
            "callsign": station.callsign,
            "name": station.name or station.callsign,
            "frequency": f"{station.frequency} {'MHz' if not is_am else 'kHz'}",
            "band": station.band,
            "erp_kw": station.erp_kw,
            "haat_m": station.haat_m,
            "city": station.city,
            "state": station.state,
            "country": station.country
        },
        "geometry": {
            "type": "Point",
            "coordinates": [round(station.longitude, 5), round(station.latitude, 5)]
        }
    })

    geojson_collection = {
        "type": "FeatureCollection",
        "features": features
    }

    # Generate Radial Cross-Section Profile (0 to 120 km)
    profile_points: List[RadialProfilePoint] = []
    max_profile_dist = max(80.0, min(180.0, calculated_tiers[-1].max_radius_km * 1.2))
    steps = 25
    step_size = max_profile_dist / steps

    for step in range(1, steps + 1):
        d_km = round(step * step_size, 1)
        if is_am:
            mvm, dbu = calculate_am_groundwave_field_strength(
                distance_km=d_km,
                power_kw=station.erp_kw,
                freq_khz=station.frequency
            )
        else:
            dbu = calculate_fm_f50_50_field_strength(
                distance_km=d_km,
                haat_m=station.haat_m,
                erp_kw=station.erp_kw
            )
            mvm = dbu_to_mvm(dbu)

        s_meter, quality, _ = assess_signal_quality(dbu, is_am)

        profile_points.append(RadialProfilePoint(
            distance_km=d_km,
            field_strength_dbu=round(dbu, 1),
            field_strength_mvm=round(mvm, 3),
            s_meter=s_meter,
            quality=quality
        ))

    return calculated_tiers, geojson_collection, profile_points


# =========================================================================
# Signal Strength Assessment & Probe
# =========================================================================

def assess_signal_quality(field_strength_dbu: float, is_am: bool = False) -> Tuple[str, str, str]:
    """
    Map field strength dBu to S-meter reading, quality description, and badge color.
    """
    if is_am:
        if field_strength_dbu >= 88.0:
            return "S9+30dB", "Pristine Urban Groundwave (Overcomes Heavy Interference)", "#10b981"
        elif field_strength_dbu >= 74.0:
            return "S9+10dB", "Strong City Grade (Clear Audio, Low Noise)", "#059669"
        elif field_strength_dbu >= 66.0:
            return "S9", "Solid Primary Service (Good Daytime Quality)", "#3b82f6"
        elif field_strength_dbu >= 54.0:
            return "S7", "Protected Rural Service (Acceptable Audio)", "#f59e0b"
        elif field_strength_dbu >= 40.0:
            return "S4", "Fringe Daytime (Noticeable Static / Atmospheric Noise)", "#8b5cf6"
        else:
            return "S1", "DX / Below Usable Threshold", "#ef4444"
    else:
        if field_strength_dbu >= 70.0:
            return "S9+20dB", "Pristine High-Fidelity Stereo (Full Quieting)", "#10b981"
        elif field_strength_dbu >= 60.0:
            return "S9", "Clear Stereo Service (Standard Home/Car Quieting)", "#3b82f6"
        elif field_strength_dbu >= 54.0:
            return "S7", "Good Mono / Light Stereo Noise (Secondary Area)", "#f59e0b"
        elif field_strength_dbu >= 48.0:
            return "S5", "Fringe / Noisy Car Radio (Suburban Boundary)", "#8b5cf6"
        elif field_strength_dbu >= 36.0:
            return "S3", "Weak / DX Reception (Requires Directional Yagi)", "#d97706"
        else:
            return "S0", "Unusable / Below Receiver Sensitivity Floor", "#ef4444"


def probe_signal_at_location(station: Station, probe_lat: float, probe_lon: float) -> SignalProbeResponse:
    """
    Calculate real-time field strength, distance, bearing, and reception quality
    at an arbitrary geographic coordinate relative to the station's transmitter.
    """
    dist_km, bearing_deg, cardinal = calculate_distance_bearing(
        station.latitude, station.longitude,
        probe_lat, probe_lon
    )
    dist_mi = round(dist_km * 0.621371, 1)

    is_am = station.band.upper() == "AM"
    power_mult = get_azimuth_power_multiplier(
        bearing_deg,
        directional=station.directional,
        beam_heading_deg=0.0
    )
    effective_erp = station.erp_kw * power_mult

    if is_am:
        mvm, dbu = calculate_am_groundwave_field_strength(
            distance_km=dist_km,
            power_kw=effective_erp,
            freq_khz=station.frequency
        )
    else:
        dbu = calculate_fm_f50_50_field_strength(
            distance_km=dist_km,
            haat_m=station.haat_m,
            erp_kw=effective_erp
        )
        mvm = dbu_to_mvm(dbu)

    s_meter, quality, badge_color = assess_signal_quality(dbu, is_am)

    unit_str = "MHz" if not is_am else "kHz"
    station_freq_str = f"{station.frequency} {unit_str}"

    notes = (
        f"Transmitter at {station.city}, {station.state} "
        f"({station.erp_kw} kW ERP, {station.haat_m}m HAAT). "
        f"Bearing from tower: {round(bearing_deg, 1)}° ({cardinal})."
    )

    return SignalProbeResponse(
        callsign=station.callsign,
        station_freq=station_freq_str,
        distance_km=round(dist_km, 1),
        distance_mi=dist_mi,
        bearing_deg=round(bearing_deg, 1),
        bearing_cardinal=cardinal,
        field_strength_dbu=round(dbu, 1),
        field_strength_mvm=round(mvm, 3),
        s_meter=s_meter,
        reception_quality=quality,
        reception_badge_color=badge_color,
        notes=notes
    )
