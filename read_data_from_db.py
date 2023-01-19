"""
Read data from influxdb database using dataframes
"""
import pandas as pd
from influxdb_client import InfluxDBClient

# You can generate a Token from the "Tokens Tab" in the UI
token = "-CdLFPnsV_raxn3j6hYrp_u9pRg-1EGTAyPh047mlL6jfVWxTX_t3PZVBS2QWfjOJLSYatMcLtNjpFe47AmmLA=="
org = "USN"
bucket = "alpide-data"

client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

query_api = client.query_api()

data_frame = query_api.query_data_frame(f'from(bucket:"{bucket}")'
                                        '|> range(start: -36h)'
                                        '|> pivot(rowKey:["_time"], columnKey:["_field"], valueColumn:"_value")'
                                        '|> keep(columns: ["x-coord", "y-coord", "z-coord"])')

pd_data_frame = pd.DataFrame(data_frame)
print('query data frame:')
print(data_frame.to_string())
print('pandas data frame')
print(pd_data_frame)