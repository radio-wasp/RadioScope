# RadioScope 📡
### US & Canadian Radio Station Coverage Map (Docker Application)

**RadioScope** is a high-precision, containerized broadcast coverage mapping web application. It generates signal contours, GIS polygons, transmitter specs, and reception predictions for any **United States (FCC)** or **Canadian (ISED)** AM/FM radio station by callsign.

![RadioScope Banner](https://img.shields.io/badge/Coverage-US%20%26%20Canada-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-emerald?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## Key Features

- **US & Canada Coverage Database**:
  - Comprehensive index of US stations (FCC) and Canadian stations (ISED/CRTC) across all states and provinces.
  - Real-world technical parameters: Coordinates, Frequency, ERP (Effective Radiated Power), HAAT (Height Above Average Terrain), Licensee, City of License, and Band.
  - Automatic synthesis engine for unindexed callsigns based on North American ITU allocations.

- **Broadcast Engineering Models**:
  - **FM Model (FCC 47 CFR § 73.313 / § 73.333 & ITU-R P.1546)**:
    - **70 dBu (3.16 mV/m)**: City Grade / Strong building penetration & mobile stereo
    - **60 dBu (1.00 mV/m)**: Principal Protected Service Area (standard car/home radio)
    - **54 dBu (0.50 mV/m)**: Secondary / Suburban Fringe reception
    - **48 dBu (0.25 mV/m)**: Weak / DX Reception boundary
  - **AM Groundwave Model (FCC 47 CFR § 73.184)**:
    - **25 mV/m**: Business / Urban Core
    - **5 mV/m**: Residential / City Grade
    - **2 mV/m**: Primary Service Area
    - **0.5 mV/m**: Protected Rural Service

- **Interactive GIS Map & Tools**:
  - Smooth multi-layer vector map (Dark Matter, Positron Light, OpenStreetMap, Satellite, OpenTopo).
  - Multi-tier contour polygons with geodesic 360-radial accuracy.
  - Pulsing transmitter beacon with tower metadata popup.
  - **Interactive Signal Strength Probe**: Click anywhere on the map to calculate exact field strength ($dB\mu V/m$ & $mV/m$), distance, bearing, and S-meter reception quality.
  - **Radial Signal Attenuation Chart**: Real-time cross-section profile of signal decay across distance.
  - **Live Web Stream Player**: Listen live to station audio broadcasts directly in the browser.
  - **Custom Transmitter Simulator**: Model hypothetical radio stations anywhere with custom power, antenna height, coordinates, and directional patterns.

- **GIS & Data Exports**:
  - **GeoJSON**: Standard polygon features for QGIS, ArcGIS, Mapbox, or Google Earth.
  - **KML**: 3D vector contours for Google Earth Desktop & Web.
  - **Engineering JSON Report**: Full technical specification and contour radius export.

---

## Quick Start with Docker

### 1. Using Docker Compose (Recommended)
```bash
cd /path/to/radio-coverage-map

# Build and run the container
docker compose up -d --build
```
Open **`http://localhost:8080`** in your browser.

To stop the container:
```bash
docker compose down
```

### 2. Using Docker CLI
```bash
# Build the Docker image
docker build -t radioscope:latest .

# Run the container on port 8080
docker run -d -p 8080:8080 --name radioscope-app radioscope:latest
```

---

## Running Locally without Docker

### Prerequisites
- Python 3.9+
- pip

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```
Open **`http://localhost:8080`** in your browser.

---

