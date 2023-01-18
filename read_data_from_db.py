"""
Read data from influxdb database
"""
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "-CdLFPnsV_raxn3j6hYrp_u9pRg-1EGTAyPh047mlL6jfVWxTX_t3PZVBS2QWfjOJLSYatMcLtNjpFe47AmmLA=="
org = "USN"
bucket = "alpide-data"

client = InfluxDBClient(url="http://localhost:8086", token=token)

query_api = client.query_api()
query = 'from(bucket:"alpide-data")\
    |> range(start: -12h)\
    |> filter(fn: (r) => r._measurement == "Coordinates")\
    |> filter(fn: (r) => r.Location == "Horten")\
    |> filter(fn: (r) => r._field == "x-coord")'

result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))
print(results)