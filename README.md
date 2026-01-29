# Containerized Task Manager

A full-stack task management application built with React, FastAPI, PostgreSQL, and RabbitMQ, all containerized with Docker.

## Prerequisites

Before you start, make sure you have the following installed on your machine:

- Docker Desktop (includes Docker and Docker Compose)
- Git (for cloning the repository)

If you don't have Docker Desktop installed, download it from https://www.docker.com/products/docker-desktop

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Containerized Task Manager
```

### 2. Start All Services

```bash
docker compose up --build
```

This command will:
- Build Docker images for backend, frontend, and worker services
- Start all services (backend, frontend, worker, nginx, postgres, rabbitmq)
- Set up networking between containers
- Initialize the PostgreSQL database

The first time you run this, it may take a few minutes to download base images and install dependencies.

### 3. Access the Application

Open your browser and navigate to:

```
http://localhost
```

You should see the Task Manager application with an input field to create tasks and a list of existing tasks.

## Using the Application

1. Type a task title in the input field
2. Click "Create Task"
3. The task will appear in the list with status PENDING
4. The worker will pick it up and change the status to PROCESSING
5. After a few seconds, the status will change to DONE
6. The frontend automatically refreshes every 3 seconds to show updates

## Project Structure

```
.
├── docker-compose.yml          # Container orchestration
├── nginx/
│   └── nginx.conf              # Reverse proxy configuration
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py             # FastAPI application
│       ├── models.py           # Database tables
│       ├── schemas.py          # Data validation
│       └── database.py         # Database connection
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── vite.config.js          # Vite configuration
│   └── src/
│       └── App.jsx             # React component
├── worker/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── worker.py               # Task worker process
└── Documentation.md            # Detailed learning notes
```

## How It Works

The application follows a microservices architecture with asynchronous task processing:

1. **Frontend (React)** - User interface for creating and viewing tasks
2. **Backend (FastAPI)** - REST API for task management, sends tasks to the queue
3. **Message Broker (RabbitMQ)** - Decouples the backend from the worker
4. **Worker (Python)** - Consumes tasks and updates their status
5. **Database (PostgreSQL)** - Persists all task data
6. **Reverse Proxy (Nginx)** - Routes requests to the appropriate service

When you create a task:
1. The frontend sends a POST request to the backend
2. The backend stores the task in the database (status: PENDING)
3. The backend sends the task ID to RabbitMQ
4. The worker picks up the task and changes status to PROCESSING
5. The worker waits 5 seconds (simulating work)
6. The worker updates the task status to DONE
7. The frontend polls the backend and displays the updated status

## Useful Commands

```bash
# View logs for a specific service
docker compose logs -f backend
docker compose logs -f frontend
docker compose logs -f worker

# View logs for all services
docker compose logs -f

# Stop all services
docker compose down

# Restart a specific service
docker compose restart frontend

# Remove all containers and volumes
docker compose down -v

# Access postgres database
docker compose exec postgres psql -U postgres -d tasksdb
```

## Making Changes During Development

### Changing Frontend Code

When you modify files in the `frontend/` folder, the changes will automatically appear in your browser thanks to Vite's hot reload feature. No need to rebuild the image.

### Changing Backend Code

Restart the backend service to pick up changes:

```bash
docker compose restart backend
```

### Changing Worker Code

Restart the worker service to pick up changes:

```bash
docker compose restart worker
```

## Service Ports

- Frontend: http://localhost (through Nginx)
- Backend API: http://localhost/api (through Nginx)
- RabbitMQ Management: http://localhost:15672 (guest/guest)
- PostgreSQL: localhost:5432

## Troubleshooting

### Port Already in Use

If you get an error about port 80 being in use, another application is using it. Either:
- Close the application using port 80
- Change the port mapping in docker-compose.yml (e.g., "8080:80")

### Services Not Starting

Check the logs for the failing service:

```bash
docker compose logs <service-name>
```

Common issues:
- Not enough disk space
- Docker daemon not running
- Port conflicts

### Database Connection Error

Make sure PostgreSQL is fully initialized:

```bash
docker compose restart postgres
docker compose restart backend
```

## Project Summary

This is a containerized full-stack application demonstrating modern web development practices. It showcases:

- Microservices architecture with independent, scalable components
- Asynchronous task processing with message queues
- Containerization using Docker and Docker Compose
- Reverse proxy routing with Nginx
- Frontend-backend communication through REST APIs
- Real-time data updates with polling
- Hot reload during development without image rebuilds
- Database persistence with volumes
- Proper service networking and dependencies

The project combines multiple technologies to create a practical, production-ready application structure suitable for both learning and real-world use cases.
