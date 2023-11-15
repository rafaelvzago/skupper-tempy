from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time

# Set up the InfluxDB client
url = "http://influxdb-service:8086"
org = "zago"
bucket = "redhat"

token = "gFXqNTnI__3YWpY1dpXioEb4CkXUvrEgSGK_P_83kJfe9tXVnGIUD1LBSe0fvCpUTo6CpyqJ4eRxVH1rcD5YJA=="

client = InfluxDBClient(url=url, token=token)

# Set up the write API
write_api = client.write_api(write_options=SYNCHRONOUS)

# Insert dummy data every 5 seconds
while True:
    p = Point("dummy_measurement").tag(
        "dummy_tag", "dummy_value").field("dummy_field", 1)
    write_api.write(bucket, org, p)
    time.sleep(5)
