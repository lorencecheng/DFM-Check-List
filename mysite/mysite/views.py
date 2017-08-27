#-*- coding:utf-8 -*-
from django.http import HttpResponse
import datetime
def index(request):
    now=datetime.datetime.now()
    current_time=str(now.hour)+":"+str(now.minute)
    html = "<html><body>It is now %s </body></html>" % current_time
    return HttpResponse("Hello world, welcome to use this DFM check list!   "+ html)
