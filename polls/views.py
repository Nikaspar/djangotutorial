from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    from datetime import datetime
    today = datetime.now()
    return HttpResponse(f'hello, {today}')