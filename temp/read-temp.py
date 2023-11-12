import paho.mqtt.client as mqtt

# MQTT Broker Configuration
mqtt_broker = "localhost"  # Use "localhost" since the MQTT broker is running on the same device
mqtt_port = 1883  # MQTT default port
mqtt_topic_celsius = "temperature/celsius"  # The MQTT topic for Celsius temperature
mqtt_topic_fahrenheit = "temperature/fahrenheit"  # The MQTT topic for Fahrenheit temperature

# Callback when a message is received
def on_message(client, userdata, message):
    print(f"Received message on topic: {message.topic}")
    print(f"Message payload: {message.payload.decode('utf-8')}")

# Create an MQTT client
client = mqtt.Client()

# Set up the message callback
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)

# Subscribe to the MQTT topics
client.subscribe([(mqtt_topic_celsius, 0), (mqtt_topic_fahrenheit, 0)])

# Start the MQTT client's loop to receive messages
client.loop_forever()
