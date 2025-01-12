# Company Management Application

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Project Setup](#project-setup)
  - [Docker Setup](#docker-setup)

## Overview

The system's primary objective is to simplify and automate the management of business entities and ensure that performance review processes are handled in an organized, secure, and efficient manner.

## Technologies Used

This project utilizes the following technologies and libraries:

- **Django** (v4.2.15): A high-level Python web framework for building robust, scalable, and secure applications.
- **Django Rest Framework** (v3.15.2): A powerful and flexible toolkit for building Web APIs with Django.
- **django-jazzmin** (v3.0.1): A modern, customizable interface for Django Admin.
- **djangorestframework-simplejwt** (v5.3.1): A library for using JSON Web Tokens (JWT) authentication with Django Rest Framework.
- **psycopg2** (v2.9.9): A PostgreSQL database adapter for Python.
- **PyJWT** (v2.9.0): A Python library to work with JSON Web Tokens (JWT), for generating and decoding JWTs.
- **Docker**: A platform for developing, shipping, and running applications inside containers, providing an isolated environment for deploying the application consistently across different environments.


### Backend

- Django: Web framework for backend development.
- Django REST Framework (DRF): Toolkit for building Web APIs.
- PostgreSQL: Relational database.
- Redis: In-memory data store for caching.
- Stripe: Payment gateway integration.
- MailHog: Email testing tool.
- JWT: JSON Web Tokens for authentication.

## Architecture

The application follows a client-server architecture with a RESTful API backend built using Django and DRF, and a React/Next.js frontend. Docker is used to containerize the application, facilitating easy deployment and scalability.

## Installation

### Prerequisites

- Docker & Docker Compose: Ensure Docker is installed on your machine. [Install Docker](https://docs.docker.com/get-docker/)


### Project Setup

1. Clone the Repository:

      git clone [https://github.com/Demo-23home/DRF_React_NextJS-Ambassador360.git](https://github.com/mennahasan19/company-task.git)
   cd App
   
2. .env File

Create a file named .env in the root directory of your project and add the following variables:
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=db
DATABASE_PORT=5432



1. **Build and Run Containers:**

### Docker Setup
docker-compose up --build
