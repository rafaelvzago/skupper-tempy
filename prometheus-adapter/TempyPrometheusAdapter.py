import time
import requests
from prometheus_client import start_http_server, Gauge

# Define Prometheus metrics
TEMPERATURE_CELSIUS = Gauge('temperature_celsius', 'Current temperature in Celsius')
TEMPERATURE_FAHRENHEIT = Gauge('temperature_fahrenheit', 'Current temperature in Fahrenheit')

def fetch_and_update_temperature():
    """Fetches temperature from the API and updates Prometheus metrics."""
    response = requests.get('http://tempy:5000/temperature')
    data = response.json()

    # Update Prometheus metrics
    TEMPERATURE_CELSIUS.set(data['celsius'])
    TEMPERATURE_FAHRENHEIT.set(data['fahrenheit'])

    print(f"Updated temperature: {data['celsius']}°C, {data['fahrenheit']}°F")

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9090)
    print("Serving metrics at :9090/metrics")
    
    # Fetch and update temperature every 10 seconds
    while True:
        fetch_and_update_temperature()
        time.sleep(10)

