# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the Python script and requirements.txt into the container
COPY influx_feeder.py requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the influx_feeder.py script when the container launches
CMD ["python", "influx_feeder.py"]