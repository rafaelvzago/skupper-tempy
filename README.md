# InfluxDB Server and Feeder

This README provides an overview of the InfluxDB feeder script and instructions for deploying InfluxDB, applying the InfluxDB service, and configuring InfluxDB settings.

## Configuring InfluxDB

Before using the feeder script, you need to configure your InfluxDB settings, including the organization, bucket, and user data. Please follow the InfluxDB documentation or use the InfluxDB CLI to configure these settings based on your requirements.


To deploy InfluxDB in your Kubernetes cluster, follow these steps:

1. Apply the InfluxDB PVC (Persistent Volume Claim) YAML file to create a persistent volume for InfluxDB data storage:

   ```bash
   kubectl apply -f influx/influxdb-pvc.yaml
   ```

2. Apply the InfluxDB Deployment YAML file to create the InfluxDB deployment:

   ```bash
   kubectl apply -f influx/influxdb-deployment.yaml
   ```

3. Apply the InfluxDB Service YAML file to create the InfluxDB service within the same namespace as your deployment:

   ```bash
   kubectl apply -f influx/influxdb-service.yaml
   ```

4. Forward the InfluxDB port using `kubectl port-forward` to access the InfluxDB API:

   ```bash
   kubectl port-forward -n influxdb deployment/influxdb 8086:8086
   ```



## InfluxDB Feeder Script

The InfluxDB feeder script (`influx_feeder.py`) is designed to insert dummy data into an InfluxDB instance at regular intervals. It uses the InfluxDB Python client library to interact with InfluxDB. The script is set to insert data every 5 seconds, and it tags and fields the data accordingly.


### Usage

To use the InfluxDB feeder script, you'll need to build and deploy a Docker image of the script. Follow these steps:

1. Make sure you have Docker installed on your system.

2. Build the Docker image using the provided Dockerfile in the same directory:

   ```bash
   docker build -t your-image-name:your-tag .
   ```

   Replace `your-image-name` and `your-tag` with appropriate values.

3. Push the Docker image to a container registry of your choice:

   ```bash
   docker push your-docker-username/your-image-name:your-tag
   ```

4. Deploy the InfluxDB feeder Docker image in your Kubernetes cluster as mentioned in the previous sections.

5. Update the InfluxDB connection details (URL and token) in the Kubernetes deployment YAML if needed.

6. Apply the Kubernetes deployment to run the InfluxDB feeder container:

   ```bash
   kubectl apply -f your-feeder-deployment.yaml
   ```

   Replace `your-feeder-deployment.yaml` with your actual deployment manifest.

The script will start inserting dummy data into your InfluxDB instance.

Before using the feeder script, you also need to configure your InfluxDB settings, including the organization, bucket, and user data. Please follow the InfluxDB documentation or use the InfluxDB CLI to configure these settings based on your requirements.


To add information about the IoT part using Raspberry Pi, a temperature sensor, and MQTT to the existing readme file in your GitHub repository, you can follow these steps. I'll provide you with the Markdown content to add to your README.md file. Make sure to replace the placeholders with actual content and URLs as needed.

# **IoT Part with Raspberry Pi, Temperature Sensor, and MQTT**

   To integrate IoT functionality into this project, we use a Raspberry Pi along with a temperature sensor to collect and transmit data via MQTT. This section provides an overview of the setup and relevant components.

   - **MQTT Configuration**

     The MQTT configuration can be found in the `mqtt/docker-compose` directory. Make sure to configure MQTT settings such as broker address, port, and authentication as needed for your setup.

   - **Scripts for IoT Data**

     We have two scripts located in the `temp/` directory to handle IoT data:

     - **Seeder Script**: This script continuously collects temperature data from the Raspberry Pi sensor and publishes it to the MQTT queue. To run this script, follow these steps:

       ```bash
       # Create a virtual environment (recommended)
       python3 -m venv venv
       source venv/bin/activate

       # Install required dependencies
       pip install -r temp/requirements.txt

       # Run the seeder script
       python temp/seeder.py
       ```

     - **Reader Script**: This script is used to test the MQTT queue by subscribing to incoming data. It helps verify that data is being transmitted correctly. To run this script, follow these steps:

       ```bash
       # Create a virtual environment (recommended)
       python3 -m venv venv
       source venv/bin/activate

       # Install required dependencies
       pip install -r temp/requirements.txt

       # Run the reader script
       python temp/reader.py
       ```

   We recommend using a virtual environment to isolate dependencies for these scripts. You can create a virtual environment using `python3 -m venv venv` and activate it with `source venv/bin/activate`.

   This IoT setup allows you to collect temperature data from your Raspberry Pi sensor and transmit it via MQTT for further processing.

2. **Contributing**

   If you have improvements or suggestions for this IoT integration, feel free to contribute to the project by submitting pull requests or raising issues.

Remember to replace the placeholders with actual content and URLs from your repository. This section provides an overview of how to add information about the IoT part using Raspberry Pi, MQTT, and temperature sensor to your README.md file.


