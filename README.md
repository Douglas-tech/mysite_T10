# mysite_T10

This README.md file provides instructions on how to build and run the application using venv and Docker.

## Prerequisites

- Python (version 3.11)
- Docker (version 20.10.8)

## Build and Run with venv

1. Clone the repository:

   ```bash
   git clone <https://douglas-tech.github.io/mysite_T10/>

Navigate to the project directory:
cd <mysite>
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate
Install the dependencies:
pip install -r requirements.txt
Run the application:
python3 app.py

Build and Run with Docker

Build the Docker image:
docker build -t mysite_t10 .
Run the Docker container:
docker run -p 8000:8000 --env-file .env mysite_t10
Access the application in your browser at http://localhost:8000.

