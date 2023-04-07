from django.shortcuts import render
from django.db.models.functions import Length
from app.models import *

# Create your views here.


def Display_Topic(request):
    LOT=Topic.objects.all()
    
    d={'topics':LOT}
    return render(request,'Display_Topic.html',d)

def Dispaly_Webpage(request):
    LOW=Webpage.objects.all()
    '''LOW=Webpage.objects.filter(Topic_name="Cricket")
    
    LOW=Webpage.objects.filter(Name="Ronaldo")
    LOW=Webpage.objects.get(Name="Ronaldo")
    #order by method
    LOW=Webpage.objects.order_by('Name')
    LOW=Webpage.objects.order_by('-Name')'''
    #length method
    LOW=Webpage.objects.order_by(Length('Name'))
    LOW=Webpage.objects.order_by(Length('Name').desc())

    d={'Web':LOW}
    return render(request,'Display_Webpage.html',d)

def Display_AccessRecord(request):
    '''LOA=AccessRecord.objects.all()
    #Field lookups
    LOA=AccessRecord.objects.all()'''
    #exclude method
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.exclude(Author='Tagore')
    LOA=AccessRecord.objects.exclude(Date='2001-09-17')
    #field lookups
    LOA=AccessRecord.objects.filter(Date__gt='2001-09-17')
    LOA=AccessRecord.objects.filter(Date__gte='2001-09-17')
    LOA=AccessRecord.objects.filter(Date__lte='2001-09-17')

    d={'AR':LOA}
    return render(request,'Display_AccessRecord.html',d)
