# My Resume Website

This repository contains the code for my personal resume website built with Flask. The website showcases my professional background, skills, and projects.

## Features

- **Home Page**: Brief introduction and professional summary.
- **About Me**: Details about my professional skills, educational background, and certifications.
- **Experience**: Overview of my professional experience and key accomplishments.
- **Projects**: Information on significant projects I've worked on, including this resume website.
- **Contact**: Form to contact me directly through the website.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework used to serve the website's backend.
- **HTML/CSS/JavaScript**: Used for the frontend to create a responsive and user-friendly interface.
- **PostgreSQL**: Database system for storing and managing application data.
- **AWS Elastic Beanstalk**: For hosting and managing the web application in the cloud.

## Local Development

Follow these instructions to set up the project locally. These steps assume you have Python and pip installed on your system.

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Setup


1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/my-resume-site.git
   cd my-resume-site

#Create and activate a virtual environment
``
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
``

#Install dependencies
``
pip install -r requirements.txt
``

#Environment Variables
``

Ensure all necessary environment variables are set, such as database URLs or any API keys.
``

#Run the application
``

flask run
``

#Access the website at http://localhost:5000.


#Deployment
This project is deployed on AWS Elastic Beanstalk. Steps to deploy:

#Prepare your application for deployment as described above.

Zip the necessary files excluding the virtual environment and any configuration files that contain sensitive information.
Upload the zip file to AWS Elastic Beanstalk through the AWS Management Console.


#Contributing

Feel free to fork the repository and submit pull requests. You can also open issues if you find any bugs or have feature suggestions.


# Resume Site Deployment Guide

This guide provides instructions on how to deploy the Resume Site application using AWS ECS, Docker, and ECR. Follow these steps to build, deploy, and manage your Dockerized application in the cloud.

## Prerequisites

- AWS CLI installed and configured with your AWS account.
- Docker installed on your local machine.
- Access to AWS ECS, ECR, and VPC services.

## Steps

### 1. Create an ECR Repository
Create a repository in Amazon ECR to store your Docker images.


$aws ecr create-repository --repository-name my-resume-site


2. Authenticate Docker with ECR
Authenticate your Docker client to your Amazon ECR registry.

$aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 285479333816.dkr.ecr.ap-southeast-2.amazonaws.com


3. Build and Tag the Docker Image
Build your Docker image locally and tag it for ECR.

$cd C:\Users\ALEKO\projects\my-resume-site
$docker build -t my-resume-site .
$docker tag my-resume-site:latest 285479333816.dkr.ecr.ap-southeast-2.amazonaws.com/my-resume-site:latest


4. Push the Docker Image to ECR
Push your tagged Docker image to the ECR repository.


$docker push 285479333816.dkr.ecr.ap-southeast-2.amazonaws.com/my-resume-site:latest


5. Create ECS Task Definition
Define how your application should run in ECS by creating a task definition.


$aws ecs register-task-definition --cli-input-json file://C:/Users/ALEKO/projects/my-resume-site/task-definition.json


6. Create an ECS Cluster
Set up an ECS cluster where your application will run.


$aws ecs create-cluster --cluster-name my-resume-site-cluster


7. Create an ECS Service
Create an ECS service to manage the running instances of your containerized application.


$aws ecs create-service --cluster my-resume-site-cluster --service-name my-resume-site-service --task-definition my-resume-site-task --desired-count 1 --launch-type FARGATE --network-configuration "awsvpcConfiguration={subnets=[subnet-id1, subnet-id2],securityGroups=[sg-id],assignPublicIp=ENABLED}" --tags key=Name,value=my-resume-site-service


8. Monitor the Service
Check the status of your service and deployments.


$aws ecs describe-services --cluster my-resume-site-cluster --services my-resume-site-service


Additional Notes

Replace placeholders like subnet-id1, subnet-id2, and sg-id with your actual VPC subnet IDs and security group IDs.

Regularly check the AWS console for logs and service status to monitor your application.


Support

For additional help or troubleshooting, please reach out to support or consult the AWS documentation for detailed guidance on ECS and ECR services.
