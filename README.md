# Enhancing Gift Recommendations Using RAG Pipeline

## Project Overview

This project provides an AI-based gift suggestion tool, which includes a backend API for gift recommendations and a frontend for user interaction. The app is containerized using Docker, and this documentation provides details on how to run the app locally and in production.
You can view our model here: http://34.219.62.77:3000/

## YouTube Link

YouTube link of our project walk through and our project demo: https://youtu.be/CSANAVumN_c

# Set-up Instructions:

## Prerequisites

- [Docker](https://www.docker.com/) (version 3.8 or above)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Access to the internet to pull necessary Docker images

## Services Overview

- **Backend**: Flask-based API to handle gift suggestion requests.
- **Frontend**: React-based user interface for interacting with the API.
- **Reverse Proxy**: (Optional for production) NGINX reverse proxy for managing traffic between the frontend and backend.

## Running the Application Locally

### Step 1: Clone the Repository

First, clone the repository:

 ⁠bash
git clone https://github.com/your-repo/gift-suggestion-app.git
cd gift-suggestion-app


### Step 2: Configure Local Docker Setup

You need to modify the `docker-compose.yml` file to run the app locally. Instead of using pre-built images, you'll need to specify the local paths for the Dockerfiles in both `backend` and `frontend` services.

1. **Backend**: Update the `backend` service in the `docker-compose.yml` file:
     ⁠yaml
    services:
      backend:
        build: ./backend  # Use local path to the Dockerfile
        container_name: gift-be
        ports:
          - "5000:5000"
        environment:
          - FLASK_ENV=development
    

⁠ 2. **Frontend**: Similarly, update the `frontend` service:
     ⁠yaml
    services:
      frontend:
        build: ./frontend  # Use local path to the Dockerfile
        container_name: gift-fe
        ports:
          - "3000:3000"
        depends_on:
          - backend
    

### Step 3: Build and Run the Containers Locally

Run the following command to build and start the containers locally:

 ⁠bash
docker-compose up --build


⁠ - The **Backend** service will be accessible at `http://localhost:5000`.
- The **Frontend** service will be accessible at `http://localhost:3000`.

### Step 4: Verify the Application

Once the containers are up and running, visit `http://localhost:3000` in your browser to interact with the frontend. The frontend will communicate with the backend API running on `http://localhost:5000`.


## Running the Application in Production

### Step 1: Pull Pre-Built Docker Images

For a production environment (such as on AWS EC2 or another hosting platform), you can pull the pre-built Docker images from Docker Hub:

 ⁠yaml
services:
  backend:
    image: namithajc/gift-be:latest
    container_name: gift-be
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production

  frontend:
    image: namithajc/gift-fe:latest
    container_name: gift-fe
    ports:
      - "3000:3000"
    depends_on:
      - backend


### Step 2: Use NGINX Reverse Proxy (Optional)

For production hosting, you can use an NGINX reverse proxy to manage traffic between the frontend and backend. The reverse proxy will forward incoming HTTP requests to the appropriate service.

 ⁠yaml
  reverse-proxy:
    image: nginx:latest
    container_name: nginx-reverse-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./certs:/etc/nginx/certs
    depends_on:
      - frontend
      - backend


### Step 3: Run the Containers in Production

To run the app in production mode:

 ⁠bash
docker-compose up -d


⁠ This will start the containers in detached mode (running in the background), and you can access your services as follows:
- The **Frontend** service will be accessible at `http://<your-production-server>:80` (via NGINX).
- The **Backend** service will be handled via NGINX and will forward requests internally.

### Step 4: Monitor the Logs

To view the logs for troubleshooting or monitoring:

 ⁠bash
docker-compose logs -f


## Stopping the Application

To stop the application:

 ⁠bash
docker-compose down
"```"

This will stop and remove the running containers.

## Additional Notes

•⁠  ⁠For local development, remember to update the ⁠ docker-compose.yml ⁠ file to use local Dockerfile paths instead of pre-built images.
•⁠  ⁠The reverse proxy section of the ⁠ docker-compose.yml ⁠ is *only required for production* (e.g., when hosting on AWS EC2 or similar).


## Key Features
- **Context-Aware Personalization:**

Tailors suggestions based on relationship type and occasion.

Dynamically adapts to user feedback and interaction history.

- **Curated and Diverse Gift Dataset:**

Specialized dataset with niche and artisanal products.

Regularly updated to reflect current trends and seasonal variations.

- **Intuitive User Interface:**

User-friendly, responsive, and customizable UI.

Users can refine recommendations based on budget, interests, and occasion 

- **Precision-Driven Metrics:**

Ensures recommendations are relevant to the context and user preferences.

## Data Sources
- **Kaggle Dataset**: Utilizes a comprehensive dataset from Kaggle featuring gift items with associated metadata.

  
## Dataset Information

Due to the size of the dataset, it has been hosted externally. You can download the complete dataset from the following link: https://drive.google.com/drive/folders/1BZFqwr6BQ-8sEdthmR2g2BcsbKosYyei

Below is a sample of our dataset:![image](https://github.com/user-attachments/assets/8182ae96-da35-440c-83af-e21ad2c9cc69)



## Contact Us:

**Amulya Murahari** 
GitHub: https://github.com/AmulyaMurahari
LinkedIn: https://www.linkedin.com/in/amulyamurahari/
Email: murahari.a@northeastern.edu

**Namitha J C**
GitHub: https://github.com/Njc27
LinkedIn: https://www.linkedin.com/in/namitha-j-c-9b478416b/
Email: jc.n@northeastern.edu

**Sinchana Kumara**
GitHub: https://github.com/SinchanaKumara
LinkedIn: https://www.linkedin.com/in/sinchanak
Email: kumara.s@northeastern.edu
