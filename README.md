# Docker
- Learnt they key concepts of docker ( images and containers) , how images are blue prints which include the code and the dependencies  , and containers are running instance of that image
- downloaded docker desktop app and pulled hello-world image and then ran the image which made a container
- learnt the basic docker commands
- learnt what dockerfile is and how they are used to create images

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