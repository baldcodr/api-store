# About
This project is a simple CI/CD pipeline to deploy a containerised FastAPI project.

# Threat Model for the System
A simple threat model has been developed and can ne accessed [here](https://github.com/baldcodr/api-store/blob/main/docs/ThreatModel.md)

# Components
1. REST API framework - FastAPI
2. Backend - Cloud Firestore 
3. Container Engine - Docker
4. Version control - GitHub
5. Package manager - poetry (optional for local development in a virtual environment)
6. IaC - Terraform
7. CI/CD - Github Actions
	- creates datastore
	- builds and publish image to Artifact repository
	- deploys application containers management service
    - picks up and deploys changes in /api and /infrastructure folders 
8. Managed Container Service - CloudRun or GKE
9. Kubernetes deployment using kustomize

# Architecture diagram
![api-store-project](docs/api-store-architecture.drawio.png?raw=true)

# Local setup using docker
1. Clone the repository and cd in to the project folder
`git clone https://github.com/baldcodr/api-store.git && cd api-store`

2. Ensure you have docker running and run the following command
`make build`

3. The appplication should be available on 0.0.0.0/8000


# Local setup using poetry
1. Ensure you have poetry installed, otherwise run the following command
`pip install poetry` or `brew install poetry`

2. Activate the poetry virtual environment
`poetry shell`

3. Install dependencies
`poetry install`

4. The appplication should be available on 0.0.0.0/8000

NB: If developing locally, add the follwoing line to your firebase.py file
`from dotenv import load_dotenv`
`load_dotenv()`
