# Use an official Python runtime as a parent image (Alpine version for minimal size)
FROM python:3.10-alpine as builder

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY TempyPrometheusAdapter.py .
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Use a multi-stage build to minimize size
FROM python:3.10-alpine

# Set the working directory to /app in the new stage
WORKDIR /app

# Copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.cache /root/.cache
COPY --from=builder /app /app

# Install dependencies using the cache from the first stage
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir requests prometheus_client && \
    rm -rf /root/.cache

# Make port 9090 available to the world outside this container
EXPOSE 9090

# Run python script when the container launches
CMD ["python3", "TempyPrometheusAdapter.py"]

