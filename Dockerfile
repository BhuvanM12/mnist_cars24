# Use the official TensorFlow image as a base image
FROM tensorflow/tensorflow:2.4.1

# Set the working directory
WORKDIR /app

# Copy the inference script and the saved model into the container
COPY inference.py /app/inference.py
COPY mnist_model.h5 /app/mnist_model.h5
# Set environment variables to configure timezone
ENV TZ=Asia/Kolkata
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages including tzdata for timezone configuration
RUN apt-get update && \
    apt-get install -y python3-opencv tzdata && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Flask
RUN pip install Flask
RUN pip install pillow

# Expose port 80
EXPOSE 80

# Command to run the inference script
ENTRYPOINT ["python3", "inference.py"]
