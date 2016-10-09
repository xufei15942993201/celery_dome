from celery import task
from celery_dome.celery import app
@app.task()
def hello_world():
    print ('this is my first celery_test')