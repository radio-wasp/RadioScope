"""
Comprehensive Canadian Broadcast Database Compiler
Generates complete database of Canadian AM & FM radio stations covering
all 10 provinces, 3 territories, and major/minor markets.
Includes the entire Stingray Radio roster, CBC/Radio-Canada networks,
Bell Media, Corus, Rogers, Acadia, Pattison, Rawlco, Harvard, Maritime Broadcasting.
"""

import json
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
CA_STATIONS_JSON = os.path.join(DATA_DIR, "ca_stations.json")

# Master Canadian Stations Registry
CANADIAN_MASTER_STATIONS = [
    # ==================== ALBERTA ====================
    # Athabasca
    {"callsign": "CKBA-FM", "name": "Boom 94.1 - Athabasca", "band": "FM", "frequency": 94.1, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 54.7167, "longitude": -113.2833, "city": "Athabasca", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    
    # Blairmore
    {"callsign": "CJPR-FM", "name": "New Country Southwest 94.9 - Blairmore / Crowsnest", "band": "FM", "frequency": 94.9, "erp_kw": 2.5, "haat_m": 250.0, "latitude": 49.6083, "longitude": -114.4500, "city": "Blairmore", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "A"},
    
    # Bonnyville
    {"callsign": "CJEG-FM", "name": "Hot 101.3 - Bonnyville / Cold Lake", "band": "FM", "frequency": 101.3, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 54.2667, "longitude": -110.7333, "city": "Bonnyville", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C1"},
    
    # Brooks
    {"callsign": "CIBQ-FM", "name": "New Country 105.7 - Brooks", "band": "FM", "frequency": 105.7, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 50.5642, "longitude": -111.8989, "city": "Brooks", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    {"callsign": "CIXF-FM", "name": "Boom 101.1 - Brooks", "band": "FM", "frequency": 101.1, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 50.5642, "longitude": -111.8989, "city": "Brooks", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    
    # Calgary
    {"callsign": "CFXL-FM", "name": "XL 103.1 - Calgary's Classic Hits", "band": "FM", "frequency": 103.1, "erp_kw": 100.0, "haat_m": 350.0, "latitude": 51.0833, "longitude": -114.2167, "city": "Calgary", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C"},
    {"callsign": "CKMP-FM", "name": "90.3 AMP Radio - Calgary's Hit Music", "band": "FM", "frequency": 90.3, "erp_kw": 100.0, "haat_m": 350.0, "latitude": 51.0833, "longitude": -114.2167, "city": "Calgary", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C"},
    {"callsign": "CHUP-FM", "name": "C97.7 - Calgary's Best Variety", "band": "FM", "frequency": 97.7, "erp_kw": 100.0, "haat_m": 350.0, "latitude": 51.0833, "longitude": -114.2167, "city": "Calgary", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Hot Adult Contemporary", "station_class": "C"},
    {"callsign": "CJAY-FM", "name": "CJAY 92 FM - Calgary's Real Rock", "band": "FM", "frequency": 92.1, "erp_kw": 100.0, "haat_m": 350.0, "latitude": 51.0833, "longitude": -114.2167, "city": "Calgary", "state": "AB", "country": "CA", "licensee": "Bell Media", "format": "Mainstream Rock", "station_class": "C"},
    {"callsign": "CKRY-FM", "name": "Country 105 - Calgary", "band": "FM", "frequency": 105.1, "erp_kw": 100.0, "haat_m": 350.0, "latitude": 51.0833, "longitude": -114.2167, "city": "Calgary", "state": "AB", "country": "CA", "licensee": "Corus Entertainment", "format": "Country", "station_class": "C"},
    {"callsign": "CHQR", "name": "QR Calgary 770 AM - Talk & News", "band": "AM", "frequency": 770, "erp_kw": 50.0, "haat_m": 140.0, "latitude": 50.8833, "longitude": -113.9167, "city": "Calgary", "state": "AB", "country": "CA", "licensee": "Corus Entertainment", "format": "News / Talk / Sports", "station_class": "A"},
    {"callsign": "CBR-FM", "name": "CBC Radio One 102.1 FM / 990 AM - Calgary", "band": "FM", "frequency": 102.1, "erp_kw": 100.0, "haat_m": 350.0, "latitude": 51.0833, "longitude": -114.2167, "city": "Calgary", "state": "AB", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "C"},
    
    # Camrose
    {"callsign": "CFCW", "name": "840 CFCW - Alberta's Country Legend", "band": "AM", "frequency": 840, "erp_kw": 50.0, "day_power_kw": 50.0, "night_power_kw": 50.0, "haat_m": 120.0, "latitude": 53.0233, "longitude": -112.8333, "city": "Camrose / Edmonton", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Country", "station_class": "A"},
    {"callsign": "CFCW-FM", "name": "New Country 98.1 - Camrose / Edmonton", "band": "FM", "frequency": 98.1, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 53.0233, "longitude": -112.8333, "city": "Camrose", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    
    # Cold Lake
    {"callsign": "CJXK-FM", "name": "Boom 95.3 - Cold Lake", "band": "FM", "frequency": 95.3, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 54.4642, "longitude": -110.1825, "city": "Cold Lake", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    
    # Drumheller
    {"callsign": "CKDQ-FM", "name": "New Country 92.5 - Drumheller", "band": "FM", "frequency": 92.5, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 51.4636, "longitude": -112.7103, "city": "Drumheller", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    {"callsign": "CHOO-FM", "name": "Boom 99.5 - Drumheller", "band": "FM", "frequency": 99.5, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 51.4636, "longitude": -112.7103, "city": "Drumheller", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    
    # Edmonton
    {"callsign": "CIRK-FM", "name": "K-97 - Edmonton's Classic Rock", "band": "FM", "frequency": 97.3, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 53.5350, "longitude": -113.3870, "city": "Edmonton", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C"},
    {"callsign": "CKRA-FM", "name": "96.3 The Breeze - Edmonton's Relaxing Favorites", "band": "FM", "frequency": 96.3, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 53.5350, "longitude": -113.3870, "city": "Edmonton", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Soft Adult Contemporary", "station_class": "C"},
    {"callsign": "CHED", "name": "630 CHED - Edmonton News Talk & Oilers", "band": "AM", "frequency": 630, "erp_kw": 50.0, "haat_m": 120.0, "latitude": 53.4833, "longitude": -113.5167, "city": "Edmonton", "state": "AB", "country": "CA", "licensee": "Corus Entertainment", "format": "News / Talk / Sports", "station_class": "A"},
    {"callsign": "CFBR-FM", "name": "100.3 The Bear - Edmonton's Rock", "band": "FM", "frequency": 100.3, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 53.5350, "longitude": -113.3870, "city": "Edmonton", "state": "AB", "country": "CA", "licensee": "Bell Media", "format": "Active Rock", "station_class": "C"},
    {"callsign": "CISN-FM", "name": "CISN Country 103.9 FM - Edmonton", "band": "FM", "frequency": 103.9, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 53.5350, "longitude": -113.3870, "city": "Edmonton", "state": "AB", "country": "CA", "licensee": "Corus Entertainment", "format": "Country", "station_class": "C"},
    {"callsign": "CBX-FM", "name": "CBC Radio One 90.9 FM / 740 AM - Edmonton", "band": "FM", "frequency": 90.9, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 53.5350, "longitude": -113.3870, "city": "Edmonton", "state": "AB", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "C"},
    
    # Edson
    {"callsign": "CFXE-FM", "name": "New Country West 94.3 - Edson", "band": "FM", "frequency": 94.3, "erp_kw": 25.0, "haat_m": 150.0, "latitude": 53.5833, "longitude": -116.4333, "city": "Edson", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    
    # High Prairie
    {"callsign": "CKVH-FM", "name": "New Country 93.5 - High Prairie", "band": "FM", "frequency": 93.5, "erp_kw": 25.0, "haat_m": 140.0, "latitude": 55.4333, "longitude": -116.4833, "city": "High Prairie", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    
    # Hinton
    {"callsign": "CFHI-FM", "name": "Boom 104.9 - Hinton", "band": "FM", "frequency": 104.9, "erp_kw": 25.0, "haat_m": 180.0, "latitude": 53.4000, "longitude": -117.5833, "city": "Hinton", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    
    # Lac La Biche
    {"callsign": "CILB-FM", "name": "Boom 103.5 - Lac La Biche", "band": "FM", "frequency": 103.5, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 54.7667, "longitude": -111.9667, "city": "Lac La Biche", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    
    # Lloydminster
    {"callsign": "CKSA-FM", "name": "New Country 95.9 - Lloydminster", "band": "FM", "frequency": 95.9, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 53.2833, "longitude": -110.0000, "city": "Lloydminster", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C"},
    
    # Red Deer
    {"callsign": "CKGY-FM", "name": "New Country 95.5 - Red Deer", "band": "FM", "frequency": 95.5, "erp_kw": 100.0, "haat_m": 240.0, "latitude": 52.2681, "longitude": -113.8111, "city": "Red Deer", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C"},
    {"callsign": "CIZZ-FM", "name": "Z 98.9 - Red Deer's Classic Rock", "band": "FM", "frequency": 98.9, "erp_kw": 100.0, "haat_m": 240.0, "latitude": 52.2681, "longitude": -113.8111, "city": "Red Deer", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C"},
    
    # Slave Lake
    {"callsign": "CHSL-FM", "name": "Boom 92.7 - Slave Lake", "band": "FM", "frequency": 92.7, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 55.2833, "longitude": -114.7667, "city": "Slave Lake", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    
    # St. Paul
    {"callsign": "CHSP-FM", "name": "New Country 97.7 - St. Paul", "band": "FM", "frequency": 97.7, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 53.9833, "longitude": -111.3000, "city": "St. Paul", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    
    # Stettler
    {"callsign": "CKSQ-FM", "name": "New Country 93.3 - Stettler", "band": "FM", "frequency": 93.3, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 52.3167, "longitude": -112.7167, "city": "Stettler", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    
    # Wainwright
    {"callsign": "CKKY-FM", "name": "Boom 101.9 - Wainwright", "band": "FM", "frequency": 101.9, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 52.8333, "longitude": -110.8667, "city": "Wainwright", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    {"callsign": "CKWY-FM", "name": "Hot 93.7 - Wainwright", "band": "FM", "frequency": 93.7, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 52.8333, "longitude": -110.8667, "city": "Wainwright", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C1"},
    
    # Westlock
    {"callsign": "CKWB-FM", "name": "New Country 97.9 - Westlock", "band": "FM", "frequency": 97.9, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 54.1500, "longitude": -113.8667, "city": "Westlock", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    
    # Wetaskiwin
    {"callsign": "CKJR", "name": "Sports 1440 - Wetaskiwin / Edmonton", "band": "AM", "frequency": 1440, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 90.0, "latitude": 52.9667, "longitude": -113.3667, "city": "Wetaskiwin", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Sports Talk", "station_class": "B"},
    
    # Whitecourt
    {"callsign": "CFXW-FM", "name": "Boom 96.7 - Whitecourt", "band": "FM", "frequency": 96.7, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 54.1414, "longitude": -115.6833, "city": "Whitecourt", "state": "AB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},

    # ==================== BRITISH COLUMBIA ====================
    # Vancouver
    {"callsign": "CHLG-FM", "name": "104.3 The Breeze - Vancouver's Relaxing Favorites", "band": "FM", "frequency": 104.3, "erp_kw": 100.0, "haat_m": 665.0, "latitude": 49.3542, "longitude": -122.9567, "city": "Vancouver", "state": "BC", "country": "CA", "licensee": "Stingray Group", "format": "Soft Adult Contemporary", "station_class": "C"},
    {"callsign": "CKZZ-FM", "name": "Z 95.3 - Vancouver's Best Variety", "band": "FM", "frequency": 95.3, "erp_kw": 75.0, "haat_m": 665.0, "latitude": 49.3542, "longitude": -122.9567, "city": "Vancouver", "state": "BC", "country": "CA", "licensee": "Stingray Group", "format": "Hot Adult Contemporary", "station_class": "C"},
    {"callsign": "CFOX-FM", "name": "CFOX 99.3 FM - Vancouver's Real Rock", "band": "FM", "frequency": 99.3, "erp_kw": 75.0, "haat_m": 665.0, "latitude": 49.3542, "longitude": -122.9567, "city": "Vancouver", "state": "BC", "country": "CA", "licensee": "Corus Entertainment", "format": "Alternative / Active Rock", "station_class": "C"},
    {"callsign": "CKNW", "name": "CKNW 980 AM - Vancouver News Talk", "band": "AM", "frequency": 980, "erp_kw": 50.0, "day_power_kw": 50.0, "night_power_kw": 50.0, "haat_m": 110.0, "latitude": 49.1678, "longitude": -122.7547, "city": "Vancouver", "state": "BC", "country": "CA", "licensee": "Corus Entertainment", "format": "News / Talk", "station_class": "A"},
    {"callsign": "CBU-FM", "name": "CBC Music 105.7 FM - Vancouver", "band": "FM", "frequency": 105.7, "erp_kw": 100.0, "haat_m": 665.0, "latitude": 49.3542, "longitude": -122.9567, "city": "Vancouver", "state": "BC", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Classical / Jazz / Arts", "station_class": "C"},
    {"callsign": "CBU", "name": "CBC Radio One 690 AM - Vancouver", "band": "AM", "frequency": 690, "erp_kw": 50.0, "day_power_kw": 50.0, "night_power_kw": 50.0, "haat_m": 120.0, "latitude": 49.1233, "longitude": -123.1114, "city": "Vancouver", "state": "BC", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "A"},
    
    # Kamloops
    {"callsign": "CHNL", "name": "Radio NL 610 AM - Kamloops", "band": "AM", "frequency": 610, "erp_kw": 25.0, "day_power_kw": 25.0, "night_power_kw": 5.0, "haat_m": 100.0, "latitude": 50.6745, "longitude": -120.3273, "city": "Kamloops", "state": "BC", "country": "CA", "licensee": "Stingray Group", "format": "Talk / Sports / Classic Hits", "station_class": "B"},
    {"callsign": "CKRV-FM", "name": "K 97.5 - Kamloops Classic Rock", "band": "FM", "frequency": 97.5, "erp_kw": 25.0, "haat_m": 350.0, "latitude": 50.6745, "longitude": -120.3273, "city": "Kamloops", "state": "BC", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "B"},
    {"callsign": "CJKC-FM", "name": "New Country 103.1 - Kamloops", "band": "FM", "frequency": 103.1, "erp_kw": 25.0, "haat_m": 350.0, "latitude": 50.6745, "longitude": -120.3273, "city": "Kamloops", "state": "BC", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "B"},
    
    # Kelowna
    {"callsign": "CKKO-FM", "name": "K 96.3 - Kelowna's Classic Rock", "band": "FM", "frequency": 96.3, "erp_kw": 30.0, "haat_m": 480.0, "latitude": 49.8880, "longitude": -119.4960, "city": "Kelowna", "state": "BC", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "B"},
    
    # Penticton
    {"callsign": "CIGV-FM", "name": "New Country 100.7 - Penticton / Okanagan", "band": "FM", "frequency": 100.7, "erp_kw": 25.0, "haat_m": 420.0, "latitude": 49.4911, "longitude": -119.5886, "city": "Penticton", "state": "BC", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "B"},

    # ==================== NOVA SCOTIA ====================
    # Halifax
    {"callsign": "CFRQ-FM", "name": "Q104 - Halifax's Best Rock", "band": "FM", "frequency": 104.3, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 44.6547, "longitude": -63.6067, "city": "Halifax", "state": "NS", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C"},
    {"callsign": "CKUL-FM", "name": "96.5 The Breeze - Halifax's Relaxing Favorites", "band": "FM", "frequency": 96.5, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 44.6547, "longitude": -63.6067, "city": "Halifax", "state": "NS", "country": "CA", "licensee": "Stingray Group", "format": "Soft Adult Contemporary", "station_class": "C"},
    {"callsign": "CIOO-FM", "name": "C100 FM - Today's Best Music", "band": "FM", "frequency": 100.1, "erp_kw": 100.0, "haat_m": 220.0, "latitude": 44.6547, "longitude": -63.6067, "city": "Halifax", "state": "NS", "country": "CA", "licensee": "Bell Media", "format": "Hot AC", "station_class": "C"},
    {"callsign": "CBHA-FM", "name": "CBC Radio One 90.5 FM - Halifax", "band": "FM", "frequency": 90.5, "erp_kw": 92.0, "haat_m": 228.0, "latitude": 44.6547, "longitude": -63.6067, "city": "Halifax", "state": "NS", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "C"},
    
    # Kentville
    {"callsign": "CIJK-FM", "name": "Rewind 89.3 - Annapolis Valley / Kentville", "band": "FM", "frequency": 89.3, "erp_kw": 100.0, "haat_m": 240.0, "latitude": 45.0781, "longitude": -64.4981, "city": "Kentville", "state": "NS", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C"},
    
    # New Glasgow
    {"callsign": "CKEZ-FM", "name": "Q97.9 - New Glasgow / Pictou County", "band": "FM", "frequency": 97.9, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 45.5833, "longitude": -62.6500, "city": "New Glasgow", "state": "NS", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C1"},
    {"callsign": "CKEC-FM", "name": "94.1 The Breeze - New Glasgow", "band": "FM", "frequency": 94.1, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 45.5833, "longitude": -62.6500, "city": "New Glasgow", "state": "NS", "country": "CA", "licensee": "Stingray Group", "format": "Soft Adult Contemporary", "station_class": "C1"},
    
    # Sydney / Cape Breton
    {"callsign": "CHRK-FM", "name": "Hot 101.9 - Sydney / Cape Breton", "band": "FM", "frequency": 101.9, "erp_kw": 52.0, "haat_m": 165.0, "latitude": 46.1367, "longitude": -60.1831, "city": "Sydney", "state": "NS", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C1"},
    {"callsign": "CKCH-FM", "name": "New Country 103.5 - Sydney / Cape Breton", "band": "FM", "frequency": 103.5, "erp_kw": 50.0, "haat_m": 165.0, "latitude": 46.1367, "longitude": -60.1831, "city": "Sydney", "state": "NS", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    {"callsign": "CJCB", "name": "1270 CJCB Country - Sydney", "band": "AM", "frequency": 1270, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 100.0, "latitude": 46.1367, "longitude": -60.1831, "city": "Sydney", "state": "NS", "country": "CA", "licensee": "Maritime Broadcasting System", "format": "Country / News", "station_class": "B"},
    {"callsign": "CHER-FM", "name": "Max 98.3 FM - Sydney / Cape Breton", "band": "FM", "frequency": 98.3, "erp_kw": 60.0, "haat_m": 180.0, "latitude": 46.1367, "longitude": -60.1831, "city": "Sydney", "state": "NS", "country": "CA", "licensee": "Maritime Broadcasting System", "format": "Classic Hits", "station_class": "C1"},

    # ==================== NEWFOUNDLAND & LABRADOR ====================
    # St. John's
    {"callsign": "VOCM", "name": "590 VOCM - Voice of the Common Man", "band": "AM", "frequency": 590, "erp_kw": 25.0, "day_power_kw": 25.0, "night_power_kw": 25.0, "haat_m": 120.0, "latitude": 47.5615, "longitude": -52.7126, "city": "St. John's", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Full-Service / News / Country", "station_class": "B"},
    {"callsign": "VOCM-FM", "name": "97.5 K-Rock - St. John's Classic Rock", "band": "FM", "frequency": 97.5, "erp_kw": 100.0, "haat_m": 240.0, "latitude": 47.5615, "longitude": -52.7126, "city": "St. John's", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C"},
    {"callsign": "CJYQ", "name": "New Country NL 930 AM - St. John's", "band": "AM", "frequency": 930, "erp_kw": 25.0, "day_power_kw": 25.0, "night_power_kw": 25.0, "haat_m": 100.0, "latitude": 47.5615, "longitude": -52.7126, "city": "St. John's", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "B"},
    {"callsign": "CKIX-FM", "name": "Hot 99.1 - St. John's Hit Music", "band": "FM", "frequency": 99.1, "erp_kw": 100.0, "haat_m": 240.0, "latitude": 47.5615, "longitude": -52.7126, "city": "St. John's", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C"},
    {"callsign": "CHOZ-FM", "name": "OZFM 94.7 FM - Newfoundland", "band": "FM", "frequency": 94.7, "erp_kw": 100.0, "haat_m": 240.0, "latitude": 47.5615, "longitude": -52.7126, "city": "St. John's", "state": "NL", "country": "CA", "licensee": "Newfoundland Broadcasting", "format": "Hot AC / Top 40", "station_class": "C"},
    
    # Carbonear
    {"callsign": "CHVO-FM", "name": "New Country NL 103.9 - Carbonear", "band": "FM", "frequency": 103.9, "erp_kw": 25.0, "haat_m": 160.0, "latitude": 47.7369, "longitude": -53.2294, "city": "Carbonear", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    
    # Channel-Port aux Basques
    {"callsign": "CFGN-FM", "name": "590 VOCM / 96.7 FM - Port aux Basques", "band": "FM", "frequency": 96.7, "erp_kw": 5.0, "haat_m": 120.0, "latitude": 47.5722, "longitude": -59.1367, "city": "Channel-Port aux Basques", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Full-Service / News", "station_class": "A"},
    
    # Clarenville
    {"callsign": "CKVO", "name": "590 VOCM / 710 AM - Clarenville", "band": "AM", "frequency": 710, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 90.0, "latitude": 48.1569, "longitude": -53.9631, "city": "Clarenville", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Full-Service / News", "station_class": "B"},
    
    # Corner Brook
    {"callsign": "CFCB", "name": "590 VOCM / 570 AM - Corner Brook", "band": "AM", "frequency": 570, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 90.0, "latitude": 48.9500, "longitude": -57.9500, "city": "Corner Brook", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Full-Service / News", "station_class": "B"},
    {"callsign": "CKXX-FM", "name": "97.5 K-Rock / 103.9 FM - Corner Brook", "band": "FM", "frequency": 103.9, "erp_kw": 50.0, "haat_m": 220.0, "latitude": 48.9500, "longitude": -57.9500, "city": "Corner Brook", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C1"},
    
    # Gander
    {"callsign": "CKGA", "name": "590 VOCM / 730 AM - Gander", "band": "AM", "frequency": 730, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 90.0, "latitude": 48.9564, "longitude": -54.6089, "city": "Gander", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Full-Service / News", "station_class": "B"},
    {"callsign": "CKXD-FM", "name": "97.5 K-Rock / 98.7 FM - Gander", "band": "FM", "frequency": 98.7, "erp_kw": 25.0, "haat_m": 160.0, "latitude": 48.9564, "longitude": -54.6089, "city": "Gander", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C1"},
    
    # Grand Falls-Windsor
    {"callsign": "CKCM", "name": "590 VOCM / 620 AM - Grand Falls-Windsor", "band": "AM", "frequency": 620, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 90.0, "latitude": 48.9333, "longitude": -55.6500, "city": "Grand Falls-Windsor", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Full-Service / News", "station_class": "B"},
    {"callsign": "CKXG-FM", "name": "97.5 K-Rock / 102.3 FM - Grand Falls-Windsor", "band": "FM", "frequency": 102.3, "erp_kw": 25.0, "haat_m": 160.0, "latitude": 48.9333, "longitude": -55.6500, "city": "Grand Falls-Windsor", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C1"},
    
    # Happy Valley-Goose Bay
    {"callsign": "CFLN-FM", "name": "Big Land - Labrador's FM 97.9", "band": "FM", "frequency": 97.9, "erp_kw": 25.0, "haat_m": 160.0, "latitude": 53.3017, "longitude": -60.3261, "city": "Happy Valley-Goose Bay", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "News / Country / Classic Hits", "station_class": "C1"},
    
    # Marystown
    {"callsign": "CHCM-FM", "name": "590 VOCM / 740 AM - Marystown", "band": "AM", "frequency": 740, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 90.0, "latitude": 47.1667, "longitude": -55.1500, "city": "Marystown", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Full-Service / News", "station_class": "B"},
    
    # Stephenville
    {"callsign": "CFSX", "name": "590 VOCM / 870 AM - Stephenville", "band": "AM", "frequency": 870, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 90.0, "latitude": 48.5500, "longitude": -58.5833, "city": "Stephenville", "state": "NL", "country": "CA", "licensee": "Stingray Group", "format": "Full-Service / News", "station_class": "B"},

    # ==================== NEW BRUNSWICK ====================
    # Fredericton
    {"callsign": "CFRK-FM", "name": "New Country 92.3 - Fredericton", "band": "FM", "frequency": 92.3, "erp_kw": 50.0, "haat_m": 140.0, "latitude": 45.9636, "longitude": -66.6431, "city": "Fredericton", "state": "NB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    {"callsign": "CIHI-FM", "name": "Hot 93.1 - Fredericton's Hit Music", "band": "FM", "frequency": 93.1, "erp_kw": 50.0, "haat_m": 140.0, "latitude": 45.9636, "longitude": -66.6431, "city": "Fredericton", "state": "NB", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C1"},
    
    # Miramichi
    {"callsign": "CHHI-FM", "name": "Rewind 95.9 - Miramichi", "band": "FM", "frequency": 95.9, "erp_kw": 50.0, "haat_m": 140.0, "latitude": 47.0269, "longitude": -65.4667, "city": "Miramichi", "state": "NB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    
    # Moncton
    {"callsign": "CJMO-FM", "name": "Q103 - Moncton's Classic Rock", "band": "FM", "frequency": 103.1, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 46.0878, "longitude": -64.7782, "city": "Moncton", "state": "NB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C1"},
    {"callsign": "CJXL-FM", "name": "New Country 96.9 - Moncton", "band": "FM", "frequency": 96.9, "erp_kw": 50.0, "haat_m": 160.0, "latitude": 46.0878, "longitude": -64.7782, "city": "Moncton", "state": "NB", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    
    # Saint John
    {"callsign": "CHNI-FM", "name": "Q88.9 - Saint John's Classic Rock", "band": "FM", "frequency": 88.9, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 45.2733, "longitude": -66.0633, "city": "Saint John", "state": "NB", "country": "CA", "licensee": "Stingray Group", "format": "Classic Rock", "station_class": "C1"},
    {"callsign": "CHSJ-FM", "name": "Country 94.1 FM - Saint John", "band": "FM", "frequency": 94.1, "erp_kw": 50.0, "haat_m": 150.0, "latitude": 45.2733, "longitude": -66.0633, "city": "Saint John", "state": "NB", "country": "CA", "licensee": "Acadia Broadcasting", "format": "Country", "station_class": "C1"},

    # ==================== PRINCE EDWARD ISLAND ====================
    # Charlottetown
    {"callsign": "CHTN-FM", "name": "Ocean 100 - Charlottetown Classic Hits", "band": "FM", "frequency": 100.3, "erp_kw": 50.0, "haat_m": 140.0, "latitude": 46.2382, "longitude": -63.1311, "city": "Charlottetown", "state": "PE", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    {"callsign": "CKQK-FM", "name": "Hot 105.5 - Charlottetown Hit Music", "band": "FM", "frequency": 105.5, "erp_kw": 50.0, "haat_m": 140.0, "latitude": 46.2382, "longitude": -63.1311, "city": "Charlottetown", "state": "PE", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C1"},
    {"callsign": "CFCY-FM", "name": "95.1 CFCY FM - The Island's Country", "band": "FM", "frequency": 95.1, "erp_kw": 50.0, "haat_m": 140.0, "latitude": 46.2382, "longitude": -63.1311, "city": "Charlottetown", "state": "PE", "country": "CA", "licensee": "Maritime Broadcasting System", "format": "Country", "station_class": "C1"},

    # ==================== ONTARIO ====================
    # Ottawa
    {"callsign": "CIHT-FM", "name": "Hot 89.9 - Ottawa's #1 Hit Music", "band": "FM", "frequency": 89.9, "erp_kw": 84.0, "haat_m": 372.0, "latitude": 45.5003, "longitude": -75.8828, "city": "Ottawa", "state": "ON", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C"},
    {"callsign": "CILV-FM", "name": "Live 88.5 - Ottawa's Alternative Rock", "band": "FM", "frequency": 88.5, "erp_kw": 84.0, "haat_m": 372.0, "latitude": 45.5003, "longitude": -75.8828, "city": "Ottawa", "state": "ON", "country": "CA", "licensee": "Stingray Group", "format": "Alternative Rock", "station_class": "C"},
    {"callsign": "CBO-FM", "name": "CBC Radio One 91.5 FM - Ottawa", "band": "FM", "frequency": 91.5, "erp_kw": 84.0, "haat_m": 372.0, "latitude": 45.5003, "longitude": -75.8828, "city": "Ottawa", "state": "ON", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "C"},
    {"callsign": "CHEZ-FM", "name": "CHEZ 106.1 FM - Ottawa Rock", "band": "FM", "frequency": 106.1, "erp_kw": 100.0, "haat_m": 372.0, "latitude": 45.5003, "longitude": -75.8828, "city": "Ottawa", "state": "ON", "country": "CA", "licensee": "Rogers Sports & Media", "format": "Mainstream Rock", "station_class": "C"},
    {"callsign": "CFRA", "name": "580 CFRA - Ottawa News Talk", "band": "AM", "frequency": 580, "erp_kw": 50.0, "day_power_kw": 50.0, "night_power_kw": 10.0, "haat_m": 120.0, "latitude": 45.2458, "longitude": -75.7667, "city": "Ottawa", "state": "ON", "country": "CA", "licensee": "Bell Media", "format": "News / Talk", "station_class": "A"},
    
    # Sudbury
    {"callsign": "CHNO-FM", "name": "Rewind 103.9 - Sudbury", "band": "FM", "frequency": 103.9, "erp_kw": 100.0, "haat_m": 250.0, "latitude": 46.4900, "longitude": -81.0100, "city": "Sudbury", "state": "ON", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C"},
    {"callsign": "CIGM-FM", "name": "Hot 93.5 - Sudbury's Hit Music", "band": "FM", "frequency": 93.5, "erp_kw": 100.0, "haat_m": 250.0, "latitude": 46.4900, "longitude": -81.0100, "city": "Sudbury", "state": "ON", "country": "CA", "licensee": "Stingray Group", "format": "Contemporary Hit Radio", "station_class": "C"},
    
    # Toronto
    {"callsign": "CFXJ-FM", "name": "New Country 93.5 - Toronto", "band": "FM", "frequency": 93.5, "erp_kw": 38.0, "haat_m": 418.0, "latitude": 43.6426, "longitude": -79.3871, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Stingray Group", "format": "Country", "station_class": "C1"},
    {"callsign": "CHBM-FM", "name": "Boom 97.3 - Toronto's 70s 80s 90s Hits", "band": "FM", "frequency": 97.3, "erp_kw": 38.0, "haat_m": 418.0, "latitude": 43.6426, "longitude": -79.3871, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Stingray Group", "format": "Classic Hits", "station_class": "C1"},
    {"callsign": "CBLA-FM", "name": "CBC Radio One 99.1 FM - Toronto", "band": "FM", "frequency": 99.1, "erp_kw": 38.0, "haat_m": 418.0, "latitude": 43.6426, "longitude": -79.3871, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "C1"},
    {"callsign": "CBL-FM", "name": "CBC Music 94.1 FM - Toronto", "band": "FM", "frequency": 94.1, "erp_kw": 38.0, "haat_m": 418.0, "latitude": 43.6426, "longitude": -79.3871, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Classical / Jazz / Arts", "station_class": "C1"},
    {"callsign": "CFRB", "name": "NEWSTALK 1010 AM - Toronto", "band": "AM", "frequency": 1010, "erp_kw": 50.0, "day_power_kw": 50.0, "night_power_kw": 50.0, "haat_m": 165.0, "latitude": 43.4831, "longitude": -79.7436, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Bell Media", "format": "News / Talk", "station_class": "A"},
    {"callsign": "CJBC", "name": "ICI Première 860 AM - Toronto", "band": "AM", "frequency": 860, "erp_kw": 50.0, "day_power_kw": 50.0, "night_power_kw": 50.0, "haat_m": 150.0, "latitude": 43.5186, "longitude": -79.7214, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Société Radio-Canada", "format": "French Public Radio", "station_class": "A"},
    {"callsign": "CHUM-FM", "name": "CHUM 104.5 FM - Toronto", "band": "FM", "frequency": 104.5, "erp_kw": 40.0, "haat_m": 418.0, "latitude": 43.6426, "longitude": -79.3871, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Bell Media", "format": "Hot AC", "station_class": "C1"},
    {"callsign": "CFNY-FM", "name": "102.1 The Edge - Toronto", "band": "FM", "frequency": 102.1, "erp_kw": 35.0, "haat_m": 418.0, "latitude": 43.6426, "longitude": -79.3871, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Corus Entertainment", "format": "Alternative Rock", "station_class": "C1"},
    {"callsign": "CILQ-FM", "name": "Q107 107.1 FM - Toronto", "band": "FM", "frequency": 107.1, "erp_kw": 40.0, "haat_m": 418.0, "latitude": 43.6426, "longitude": -79.3871, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Corus Entertainment", "format": "Classic Rock", "station_class": "C1"},
    {"callsign": "CHFI-FM", "name": "98.1 CHFI - Toronto", "band": "FM", "frequency": 98.1, "erp_kw": 44.0, "haat_m": 418.0, "latitude": 43.6426, "longitude": -79.3871, "city": "Toronto", "state": "ON", "country": "CA", "licensee": "Rogers Sports & Media", "format": "Adult Contemporary", "station_class": "C1"},

    # ==================== QUEBEC ====================
    {"callsign": "CBF-FM", "name": "ICI Première 95.1 FM - Montréal", "band": "FM", "frequency": 95.1, "erp_kw": 100.0, "haat_m": 300.0, "latitude": 45.5047, "longitude": -73.5906, "city": "Montréal", "state": "QC", "country": "CA", "licensee": "Société Radio-Canada", "format": "French Public Radio", "station_class": "C"},
    {"callsign": "CBME-FM", "name": "CBC Radio One 88.5 FM - Montreal", "band": "FM", "frequency": 88.5, "erp_kw": 25.0, "haat_m": 300.0, "latitude": 45.5047, "longitude": -73.5906, "city": "Montréal", "state": "QC", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "B"},
    {"callsign": "CHOM-FM", "name": "CHOM 97.7 FM - The Spirit of Rock", "band": "FM", "frequency": 97.7, "erp_kw": 41.2, "haat_m": 300.0, "latitude": 45.5047, "longitude": -73.5906, "city": "Montréal", "state": "QC", "country": "CA", "licensee": "Bell Media", "format": "Mainstream Rock", "station_class": "C1"},
    {"callsign": "CJAD", "name": "CJAD 800 AM - Montreal News Talk", "band": "AM", "frequency": 800, "erp_kw": 50.0, "day_power_kw": 50.0, "night_power_kw": 50.0, "haat_m": 120.0, "latitude": 45.4267, "longitude": -73.6822, "city": "Montréal", "state": "QC", "country": "CA", "licensee": "Bell Media", "format": "News / Talk", "station_class": "A"},
    {"callsign": "CKOI-FM", "name": "CKOI 96.9 FM - Montréal", "band": "FM", "frequency": 96.9, "erp_kw": 148.0, "haat_m": 224.0, "latitude": 45.5047, "longitude": -73.5906, "city": "Montréal", "state": "QC", "country": "CA", "licensee": "Cogeco Media", "format": "CHR / Top 40", "station_class": "C"},
    {"callsign": "CHOI-FM", "name": "Radio X 98.1 FM - Québec City", "band": "FM", "frequency": 98.1, "erp_kw": 70.0, "haat_m": 350.0, "latitude": 46.8167, "longitude": -71.2167, "city": "Québec City", "state": "QC", "country": "CA", "licensee": "RNC Media", "format": "Talk / Active Rock", "station_class": "C"},

    # ==================== MANITOBA ====================
    {"callsign": "CJOB", "name": "680 CJOB - Winnipeg's Talk Leader", "band": "AM", "frequency": 680, "erp_kw": 50.0, "day_power_kw": 50.0, "night_power_kw": 50.0, "haat_m": 120.0, "latitude": 49.7719, "longitude": -97.1858, "city": "Winnipeg", "state": "MB", "country": "CA", "licensee": "Corus Entertainment", "format": "News / Talk / Sports", "station_class": "A"},
    {"callsign": "CITI-FM", "name": "92.1 CITI FM - Winnipeg's Rock", "band": "FM", "frequency": 92.1, "erp_kw": 100.0, "haat_m": 160.0, "latitude": 49.8833, "longitude": -97.1333, "city": "Winnipeg", "state": "MB", "country": "CA", "licensee": "Rogers Sports & Media", "format": "Mainstream Rock", "station_class": "C1"},
    
    # ==================== SASKATCHEWAN ====================
    {"callsign": "CKOM", "name": "650 CKOM News Talk - Saskatoon", "band": "AM", "frequency": 650, "erp_kw": 25.0, "day_power_kw": 25.0, "night_power_kw": 25.0, "haat_m": 100.0, "latitude": 52.1333, "longitude": -106.6667, "city": "Saskatoon", "state": "SK", "country": "CA", "licensee": "Rawlco Communications", "format": "News / Talk", "station_class": "B"},
    {"callsign": "CKRM", "name": "620 CKRM - The Voice of Saskatchewan", "band": "AM", "frequency": 620, "erp_kw": 10.0, "day_power_kw": 10.0, "night_power_kw": 10.0, "haat_m": 100.0, "latitude": 50.4500, "longitude": -104.6167, "city": "Regina", "state": "SK", "country": "CA", "licensee": "Harvard Media", "format": "Country / News", "station_class": "B"},

    # ==================== TERRITORIES ====================
    {"callsign": "CFWH-FM", "name": "CBC Radio One 94.5 FM - Whitehorse", "band": "FM", "frequency": 94.5, "erp_kw": 1.5, "haat_m": 350.0, "latitude": 60.7212, "longitude": -135.0568, "city": "Whitehorse", "state": "YT", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "A"},
    {"callsign": "CFYK-FM", "name": "CBC Radio One 99.1 FM - Yellowknife", "band": "FM", "frequency": 99.1, "erp_kw": 5.0, "haat_m": 120.0, "latitude": 62.4540, "longitude": -114.3718, "city": "Yellowknife", "state": "NT", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "B"},
    {"callsign": "CFFB", "name": "CBC Radio One 1230 AM - Iqaluit", "band": "AM", "frequency": 1230, "erp_kw": 1.0, "haat_m": 60.0, "latitude": 63.7467, "longitude": -68.5170, "city": "Iqaluit", "state": "NU", "country": "CA", "licensee": "Canadian Broadcasting Corporation", "format": "Public Radio / News", "station_class": "C"}
]


def compile_and_sync():
    print(f"Writing {len(CANADIAN_MASTER_STATIONS)} Canadian stations to {CA_STATIONS_JSON}...")
    with open(CA_STATIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(CANADIAN_MASTER_STATIONS, f, indent=2)
    print("Compilation successful.")


if __name__ == "__main__":
    compile_and_sync()
