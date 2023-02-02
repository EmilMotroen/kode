'''
Make a background process that will write to the database over time
run with pythonw instead of python
'''
from datetime import datetime
from time import sleep

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import numpy as np
from threading import Thread

def write_to_db():
    alpide_id = 0  # Z-akse
    while True:
        x = np.random.randint(0, 513)
        y = np.random.randint(0, 1025)
        point = Point("Coordinates")\
            .tag("Location", "Horten")\
            .field("X", x)\
            .field("Y", y)\
            .field("ALPIDE-ID", alpide_id)\
            .time(datetime.utcnow(), WritePrecision.NS)
        try:
            write_api.write(bucket, org, point)  # Skriver til database
        except Exception:
            break
        alpide_id += 1
        if alpide_id == 7:  # 8 ALPIDEs stacked
            alpide_id = 0
            sleep(300)  # 5 minutter mellom hver sending
        

def create_thread():
    daemon = Thread(target=write_to_db(), daemon=True, name='WritingToDB')
    daemon.start()

# You can generate a Token from the "Tokens Tab" in the UI
token = "Z1O3pS-GV2Mf0KJi4TVpcn22D_fZ4Hi3eTj8DGPbFQVrfb1FIkUbg1Cn_BPd8SB0VARDNDvqdYr1luqy6teCHw=="
org = "USN"
bucket = "alpide-data"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)
create_thread()