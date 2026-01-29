from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import json
import pika

from app import models, schemas
from app.database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    new_task = models.Task(
        title=task.title,
        status="PENDING"
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    send_task_to_queue(new_task.id)
    return new_task


@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

def send_task_to_queue(task_id: int):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    )
    channel = connection.channel()

    channel.queue_declare(queue="task_queue")

    message = json.dumps({"task_id": task_id})
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message
    )

    connection.close()
