import os
import glob
import time
import datetime
import paho.mqtt.client as mqtt

# MQTT Broker Configuration
mqtt_broker = "localhost"  # Use "localhost" since the MQTT broker is running on the same device
mqtt_port = 1883  # MQTT default port
mqtt_topic = "temperature"  # The MQTT topic to publish temperature readings

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    try:
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            # Formatting the temperature output to 2 decimal places
            temp_c = "{:.2f}".format(temp_c)
            temp_f = "{:.2f}".format(temp_f)
            # Prometheus format
            temp_c_prometheus = "temp_c{sensor=\"28-000005b2b3f1\"} " + str(temp_c)
            temp_f_prometheus = "temp_f{sensor=\"28-000005b2b3f1\"} " + str(temp_f)

            # Get the current timestamp
            timestamp = int(time.time())

            # MQTT publish with timestamp
            publish_to_mqtt(f"{temp_c_prometheus} {timestamp}", f"{temp_f_prometheus} {timestamp}")

            return timestamp, temp_c, temp_f
    except Exception as e:
        # continue
        print(f"Error: {str(e)}")


def publish_to_mqtt(temp_c, temp_f):
    try:
        client = mqtt.Client()
        client.connect(mqtt_broker, mqtt_port, 60)
        client.publish(mqtt_topic + "/celsius", temp_c)
        client.publish(mqtt_topic + "/fahrenheit", temp_f)
        client.disconnect()
        print("Published to MQTT successfully.")
    except Exception as e:
        print(f"MQTT publish error: {str(e)}")


while True:
	print(read_temp())
	time.sleep(1)
