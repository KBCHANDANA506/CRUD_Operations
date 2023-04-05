from django.shortcuts import render

from app.models import *

# Create your views here.


def Display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'Display_Topic.html',d)

def Dispaly_Webpage(request):
    LOW=Webpage.objects.all()
    d={'Web':LOW}
    return render(request,'Display_Webpage.html',d)

def Display_AccessRecord(request):
    LOA=AccessRecord.objects.all()
    d={'AR':LOA}
    return render(request,'Display_AccessRecord.html',d)