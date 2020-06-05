from django.shortcuts import render
import datetime

def home(request):
    name = 'Dave'
    date = datetime.datetime.utcnow()
    cntxt = {'name': name, 'date': date}
    return render(request, 'home.html', cntxt)