这里我们建一个名为celery_demo的项目和celery_app应用。
1.编辑settings.py文件

在文件的最后添加如下代码：

###配置Broker
BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_TRANSPORT = 'redis'

2.新建celery.py文件

from __future__ import absolute_import

import os
import django

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

app = Celery('demo')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

3.新建tasks.py文件

在home应用文件夹下：

from demo.celery import app

@app.task
def hello_world():
    print('Hello World')

4.编辑viewss.py文件

#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

from .tasks import hello_world

def index(request):
    hello_world.delay()
    return HttpResponse(u"Fuck the GFW!")

5.其他

当然别忘了在app_installed注册celery_app应用，并且配置url.py的路由。
6.启动Celery和Django

进入celery_demo工程下,启动Celery。

$ celery -A demo worker -l debug

启动Django：

$ python manage.py runserver

7.大功告成

打开浏览器，进入index方法，可看到Celery日志打印了”Hello World“
