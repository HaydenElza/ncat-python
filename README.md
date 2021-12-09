# ncat-python

Python Bindings for NGS Coordinate Conversion and Transformation Tool (NCAT).

NCAT: https://geodesy.noaa.gov/NCAT/
NCAT Web Services Docs: https://geodesy.noaa.gov/web_services/ncat/index.shtml

## Installation

Install using pip:
```bash
pip install ncat
```

## Quickstart

```python
from ncat import ncat

response = ncat.llh(39.2240867222, -98.5421515000, 'nad83(1986)', 'nad83(2011)')

print('lat:', response['destLat'])
print('lon:', response['destLon'])
```

## Services

### [Latitude-Longitude-Height](https://geodesy.noaa.gov/web_services/ncat/lat-long-height-service.shtml)
```python
ncat.llh(lat, lon, in_datum, out_datum, eht=None, spc_zone=None, utm_zone=None, a=None, invf=None, in_vert_datum=None, out_vert_datum=None, ortho_ht=None)
```

### [State Plance Coordinates (SPC)](https://geodesy.noaa.gov/web_services/ncat/spc-service.shtml)
```python
ncat.spc(northing, easting, in_datum, out_datum, spc_zone, units=None, utm_zone=None, eht=None, in_vert_datum=None, out_vert_datum=None, ortho_ht=None)
```

### [Universal Transverse Mercator (UTM)](https://geodesy.noaa.gov/web_services/ncat/utm-service.shtml)
```python
ncat.utm(northing, easting, in_datum, out_datum, utm_zone, hemi=None, a=None, invf=None, spc_zone=None, eht=None, in_vert_datum=None, out_vert_datum=None, ortho_ht=None)
```

### [Cartesian Coordinates (XYZ)](https://geodesy.noaa.gov/web_services/ncat/xyz-service.shtml)
```python
ncat.xyz(x, y, z, in_datum, out_datum, spc_zone=None, utm_zone=None, a=None, invf=None)
```

### [U.S. National Grid (USNG)](https://geodesy.noaa.gov/web_services/ncat/usng-service.shtml)
```python
ncat.usng(usng, in_datum, out_datum, spc_zone=None, a=None, invf=None, eht=None, in_vert_datum=None, out_vert_datum=None, ortho_ht=None)
```