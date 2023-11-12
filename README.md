
# InfluxDB Server and Feeder README

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


