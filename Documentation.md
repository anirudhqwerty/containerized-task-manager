
# Docker
- Learnt they key concepts of docker ( images and containers) , how images are blue prints which include the code and the dependencies  , and containers are running instance of that image
- downloaded docker desktop app and pulled hello-world image and then ran the image which made a container
- learnt the basic docker commands
- learnt what dockerfile is and how they are used to create images

---

# FastAPI
- revised basic concepts  , GET and POST requests
- learnt the fundamentals of REST API ,the rules it follows which makes an API a REST API , and how it is important for scalable apps which have server to client and vice versa communication
## How FastAPI talks to the Database
### SQLAlchemy
- it is a python library that lets python talk to the database
- what happens is that i will write python and SQLAlchemy will convert it into SQL
### Fast API + SQLAlchemy
- now FastAPI doesn't keep the connection to the database open forever instead there are sessions.
- Whenever a request has to be made , a session is opened and then request is handeled and the session gets used/closed.

Most of the FastAPI apps look like this :
 ```
    app/
    ├── main.py        ← FastAPI app
    ├── database.py    ← engine + session
    ├── models.py      ← SQLAlchemy tables
    └── schemas.py     ← Pydantic models
```
- database.py - it connects to the database ,creates db sessions per request and then ensures the connection is closed
- model.py - creates table "task"
- schemas.py - makes sure the shape and format of the incoming data is correct
- main.py - FastAPI app 
---
# RabbitMQ
- it is a message broker program which ensures asynchronous communication between different different parts of system
- it does so by storing the messages in a queue
- there is a Producer(program which sends the message) , Queue(waiting line which holds the message), Consumer( program which recieves the message) and the Broker which is RabbitMQ itself
- RabbitMQ stores a message for an indefinite period of time , the message will only stay in the queue until the consumer takes it
- in this project , the backend is Producer and workers are the consumers , message is the task_id
### now practically learning what it does
- downloaded pika library , what it does is that it lets python talk to RabbitMQ
- wrote a function which connects to RabbitMQ and sends the takss id as a message into a queue

# Worker
- worker is just a python program that does the task
```
Backend - creates the task
RabbitMQ - holds the task
Worker - does the task
```
- in this project , the task for the worker is just to read the task, simulate processing by added fake waiting , and then update db status to DONE.

# Nginx
- from what i have understood is that it simplifies the mess , because frontend is on one port and backend is on another , so nginx is a program which checks what i am asking for — if i ask for the website (/) it sends me to the frontend container, and if i ask for data (/api) it sends me to the backend container.
- it is at port 80 , so if i can simply go to http://localhost  , and dont have to remember different ports such as 8000 or 3000
