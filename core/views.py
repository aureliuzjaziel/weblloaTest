from django.shortcuts import render, HttpResponse
from places.models import Place


# Create your views here.
def home(request): 
    places=Place.objects.all()
    return render(request,'core/index.html',{'places':places})
