"""
Write data to an influxdb database

Launch influx with 
    cd C:\'Program Files'\InfluxData\influxdb
    ./influxdb
in powershell
"""
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import numpy as np

# You can generate a Token from the "Tokens Tab" in the UI
token = "Z1O3pS-GV2Mf0KJi4TVpcn22D_fZ4Hi3eTj8DGPbFQVrfb1FIkUbg1Cn_BPd8SB0VARDNDvqdYr1luqy6teCHw=="
org = "USN"
bucket = "alpide-data"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)
points = []
x = np.random.randint(-4, 12)
y = np.random.randint(-12, 4)
alpide_id = 0  # Z-akse
i = 0
while i != 10:
    point = Point("Coordinates")\
        .tag("Location", "Horten")\
        .field("X", x)\
        .field("Y", y)\
        .field("ALPIDE-ID", alpide_id)\
        .time(datetime.utcnow(), WritePrecision.NS)
    try:
        write_api.write(bucket, org, point)  # Skriver til database
    except Exception as e:
        print(f'Exception caught: {e}')
        break
    i += 1
    x -= 2
    y += 3
    alpide_id += 1

print('...ferdig')