# TFM Demo Application

Demo application for the Master's Thesis "Design and Implementation of a DevSecOps Architecture Based on GitOps".

This repository contains the source code for the demo application and the Continuous Integration (CID) pipeline (GitHub Actions) that builds the image, runs vulnerability scans with Trivy, generates a SBOM with Syft+Grype, and publishes the image to Quay.io.

## Structure

- `app/` — Python (Flask) source code
- `docker/` — Dockerfiles (secure and vulnerable versions for testing)
- `.github/workflows/` — GitHub Actions pipeline

## CI/CD Pipeline

The pipeline is automatically triggered with each push to the `main` branch. If the Trivy scan detects CRITICAL or HIGH vulnerabilities with available fixes, the pipeline fails and the image is not published.

## Related Repositories

- GitOps Repository (Kubernetes manifestos): https://github.com/ezixd23/tfm-gitops

## Author

Ziad El Karrabi El Hanafi — Master's Thesis, 2026
