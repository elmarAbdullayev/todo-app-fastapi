# Todo App API (FastAPI)

> A secure backend API built with FastAPI for managing personal tasks with user authentication and authorization.

This project is a **RESTful Todo application backend** built using FastAPI. It includes **JWT authentication**, **user registration/login**, and **CRUD operations for tasks**. Each user can only access their own tasks.

---

## Features

### Authentication

* User registration
* Secure login with JWT token
* Password hashing with bcrypt (Passlib)
* Protected routes using OAuth2

### Task Management (CRUD)

* Create tasks
* Get all user tasks
* Get single task by ID
* Update tasks
* Delete tasks
* User-based data isolation

---

## Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy
* MySQL / PyMySQL
* JWT (python-jose)
* Passlib (bcrypt hashing)
* Pydantic Settings
* Uvicorn

---

## Architecture Overview

```text id="todo_arch"
FastAPI App
│
├── Authentication Layer
│   ├── Register
│   ├── Login (JWT)
│   └── Current User Dependency
│
├── Task Module
│   ├── Create Task
│   ├── Read Tasks
│   ├── Update Task
│   └── Delete Task
│
├── Database Layer
│   ├── Users Table
│   ├── Tasks Table
│   └── SQLAlchemy ORM
│
Security
├── Password Hashing (bcrypt)
├── JWT Token Authentication
└── OAuth2PasswordBearer
```

---

## Database Models

### User

* id
* username (unique)
* password (hashed)
* relationship → tasks

### Task

* id
* title
* description
* completed
* user_id (foreign key)

---

## API Endpoints

### Authentication

| Method | Endpoint    | Description                 |
| ------ | ----------- | --------------------------- |
| POST   | `/register` | Register new user           |
| POST   | `/login`    | Login and receive JWT token |

---

### Tasks (Protected Routes)

All task endpoints require a valid JWT token.

| Method | Endpoint            | Description        |
| ------ | ------------------- | ------------------ |
| POST   | `/erstell_task`     | Create a new task  |
| GET    | `/get_all_tasks`    | Get all user tasks |
| GET    | `/get_task/{id}`    | Get single task    |
| PUT    | `/put_task/{id}`    | Update task        |
| DELETE | `/delete_task/{id}` | Delete task        |

---

## Authentication Flow

1. User registers with username + password
2. Password is hashed (bcrypt)
3. User logs in
4. Server returns JWT token
5. Token is sent in request headers
6. `get_current_user` validates token
7. User can access only their own tasks

---

## Security Features

* Password hashing (bcrypt)
* JWT token authentication
* Expiration time for tokens
* Protected routes using dependencies
* User-based access control (no cross-user access)

---

## Environment Variables (.env)

```env id="env_todo"
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
```

---

## Installation

### 1. Clone repository

```bash id="clone_todo"
git clone https://github.com/yourusername/todo-fastapi.git
cd todo-fastapi
```

---

### 2. Create virtual environment

```bash id="venv_todo"
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 3. Install dependencies

```bash id="install_todo"
pip install -r requirements.txt
```

---

### 4. Run server

```bash id="run_todo"
uvicorn app.main:app --reload
```

---

## Key Learnings

This project demonstrates:

* FastAPI backend development
* REST API design
* JWT authentication system
* Secure password handling (bcrypt)
* SQLAlchemy ORM relationships
* Dependency injection system in FastAPI
* User authorization logic
* Clean backend architecture

---

## Possible Improvements

* Role-based access control (Admin/User)
* Refresh tokens system
* Frontend integration (React/Vue)
* Docker containerization
* Unit & integration testing (pytest)
* PostgreSQL migration
* Swagger API improvements

---

## Author

Developed as a learning project to understand secure backend development using FastAPI, authentication systems, and database relationships.
