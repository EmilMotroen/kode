"""
Read data from influxdb database
"""
import pandas as pd
import matplotlib.pyplot as plt
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "-CdLFPnsV_raxn3j6hYrp_u9pRg-1EGTAyPh047mlL6jfVWxTX_t3PZVBS2QWfjOJLSYatMcLtNjpFe47AmmLA=="
org = "USN"
bucket = "alpide-data"

client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

query_api = client.query_api()

data_frame = query_api.query_data_frame('from(bucket:"alpide-data")'
                                        '|> range(start: -12h)'
                                        '|> pivot(rowKey:["_time"], columnKey:["_field"], valueColumn:"_value")')
                                        #'|> keep(columns: ["x-coord", "y-coord", "z-coord"])')
print(data_frame.to_string())