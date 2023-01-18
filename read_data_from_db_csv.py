"""
Read data from influxdb database using csv
"""
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "-CdLFPnsV_raxn3j6hYrp_u9pRg-1EGTAyPh047mlL6jfVWxTX_t3PZVBS2QWfjOJLSYatMcLtNjpFe47AmmLA=="
org = "USN"
bucket = "alpide-data"

client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

query_api = client.query_api()
query = 'from(bucket:"alpide-data")\
    |> range(start: -12h)\
    |> filter(fn: (r) => r._measurement == "Coordinates"'

csv_results = query_api.query_csv('from(bucket: "alpide-data") |> range(start: -12h)')
val_count = 0
for line in csv_results:
    if not len(line) == 0:
        print(f'{line}') 