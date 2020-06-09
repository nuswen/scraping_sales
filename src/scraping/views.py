from django.shortcuts import render
from .models import Vacancy

def home_view(request):
    print(request.GET)
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs =[]
    flt = {}   
    if city:
        flt['city__name'] = city
    if language:
        flt['language__name'] = language
    qs = Vacancy.objects.filter(**flt)
    return render(request,'scraping/home.html',{'object_list':qs})