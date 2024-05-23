# mnist_cars24
# MNIST Handwritten Digit Recognition

This repository contains scripts and configurations for building a machine learning model to recognize handwritten digits using the MNIST dataset.

## Contents

- [Description](#description)
- [Files](#files)
- [Usage](#usage)
- [Deployment](#deployment)


## Description

The goal of this project is to train a machine learning model to accurately classify handwritten digits and deploy it as a RESTful API endpoint using Docker and Kubernetes.

## Files

- **Dockerfile**: Contains instructions to build a Docker image for the inference service.
- **inference.py**: Script to perform inference using the trained model.
- **mnist_model.h5**: Trained model file.
- **model_training.py**: Script to train the machine learning model.
- **deployment.yaml**: Kubernetes deployment configuration.
- **service.yaml**: Kubernetes service configuration.

## Usage

To train the model locally, run `model_training.py` script. This will generate the `mnist_model.h5` file.

To deploy the model as a RESTful API endpoint:

1. Build the Docker image using the provided Dockerfile.
2. Deploy the Docker image to Kubernetes using the provided deployment.yaml and service.yaml files.

## Deployment

Ensure you have Docker and Kubernetes installed locally. Then, follow the steps mentioned in the [Usage](#usage) section to deploy the model.

