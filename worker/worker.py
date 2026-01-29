import json
import time
import pika
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:qwerty@postgres:5432/tasksdb"
engine = create_engine(DATABASE_URL)

def process_task(ch, method, properties, body):
    data = json.loads(body)
    task_id = data["task_id"]

    print(f"Processing task {task_id}")

    time.sleep(5)

    with engine.begin() as conn:
        conn.execute(
            text("UPDATE tasks SET status = 'DONE' WHERE id = :id"),
            {"id": task_id}
        )

    print(f"Task {task_id} marked as DONE")

    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host="rabbitmq")
            )
            break
        except Exception as e:
            print("Waiting for RabbitMQ...", e)
            time.sleep(3)
    channel = connection.channel()

    channel.queue_declare(queue="task_queue")

    print("Worker waiting for tasks...")

    channel.basic_consume(
        queue="task_queue",
        on_message_callback=process_task
    )

    channel.start_consuming()

if __name__ == "__main__":
    main()
