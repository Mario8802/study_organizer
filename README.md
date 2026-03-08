# Study Organizer – Django Web Application

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Docker-blue)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

## Overview

Study Organizer is a web application built with the Django framework that helps students manage their academic activities. The application allows users to organize courses, schedule lectures, and track tasks with deadlines.

The project demonstrates the use of Django models, forms, class-based views, template inheritance, and PostgreSQL integration.

The goal of the application is to provide a simple and structured way to keep track of academic responsibilities in one place.

---

## Features

* Manage university **courses**
* Schedule **lectures** associated with courses
* Create and track **tasks and deadlines**
* Mark tasks as completed
* Automatically display remaining days until a task deadline
* Custom **404 error page**
* Responsive interface using **Bootstrap**
* Clean navigation between all pages

---

## Project Structure

The application is organized into three Django apps:

* **courses** – manages course information
* **schedule** – handles lectures and lecture scheduling
* **tasks** – manages assignments and deadlines

---

## Database

The project uses **PostgreSQL** as the database management system.

PostgreSQL is run inside a **Docker container** for easier setup and portability.

---

## Technologies Used

* Python
* Django
* PostgreSQL
* Docker
* Bootstrap
* HTML / CSS

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Mario8802/study_organizer.git
cd study_organizer
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start PostgreSQL using Docker

```bash
docker run -d -p 5432:5432 \
-e POSTGRES_DB=study_organizer_db \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=postgres \
--name study_postgres postgres
```

---

### 5. Apply migrations

```bash
python manage.py migrate
```

---

### 6. Create admin user (optional)

```bash
python manage.py createsuperuser
```

---

### 7. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```
http://127.0.0.1:8000/
```

---

## Custom Functionality

The application includes several custom features required for the project:

* Custom **form validation**
* Custom **template filter** for displaying remaining days until a deadline
* **Disabled form fields**
* **Delete confirmation pages**
* **Bootstrap styled forms**
* **Custom 404 error page**

---

## Notes

Authentication and Django user management are intentionally excluded as required by the project specification.

---

## Author

Project developed as part of the **Django Web Development coursework**.
