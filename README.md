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
