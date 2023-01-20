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

# You can generate a Token from the "Tokens Tab" in the UI
token = "-CdLFPnsV_raxn3j6hYrp_u9pRg-1EGTAyPh047mlL6jfVWxTX_t3PZVBS2QWfjOJLSYatMcLtNjpFe47AmmLA=="
org = "USN"
bucket = "alpide-data"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

x = -1
y = 4
z = -5
i = 0
points = []
while i < 10:
    point = Point("Coordinates")\
        .tag("Location", "Horten")\
        .field("x-coord", x)\
        .field("y-coord", y)\
        .field("z-coord", z)\
        .time(datetime.utcnow(), WritePrecision.NS)
    points.append(point)
    
    x -= 1
    y += 1
    z += 2
    i += 1
write_api.write(bucket, org, points)  # Skriver til database
print('...ferdig')