from time import sleep
import logging

from fastapi import FastAPI, BackgroundTasks

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

def send_email(message):
    sleep(5)
    print(message)

@app.get("/async")
async def index(background_tasks: BackgroundTasks):
    # send_email()
    background_tasks.add_task(send_email, 'Test')
    background_tasks.add_task(send_email, 'Test1')
    return {'result': 'success'}, 200

@app.get("/sync")
async def index():
    send_email('test')
    # background_tasks.add_task(send_email, 'Test')
    return {'result': 'success'}, 200
