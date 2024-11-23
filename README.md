# GCP Pipeline Project

A containerized application pipeline using Google Cloud Platform's Cloud Build service.

## Description

This project implements a continuous integration pipeline using Google Cloud Build to automatically build and push Docker containers to Google Container Registry (GCR).

## Features

- Automated Docker image builds
- Cloud-native logging integration
- Container versioning using commit SHA
- Google Container Registry integration

## Installation

1. Set up a Google Cloud Platform account
2. Enable required APIs:
   - Cloud Build API
   - Container Registry API
3. Install Google Cloud SDK

## Usage

The pipeline automatically triggers on repository changes. To manually trigger a build:


gcloud builds submit --config cloudbuild.yaml


