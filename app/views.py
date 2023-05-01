from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def inserttopic(request):
    if request.method=='POST':                                                
        topicname=request.POST['topic_name']
        TO=Topic.objects.get_or_create(topic_name=topicname)[0]
        TO.save()
        return HttpResponse('insert data is done successfully')

    return render(request,'inserttopic.html')


def insertwebpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']

        TO=Topic.objects.get(topic_name=topic)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('insert webpage objects successfully')


    return render(request,'insertwebpage.html',d)

def insertaccess(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']

        WO=Webpage.objects.get(name=name)

        AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]

        AO.save()

        return HttpResponse('insert accessrecord is done successfully')

    return render(request,'insertaccess.html',d)



def retrievedata(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)

        d1={'webpages':webqueryset}
        return render(request,'displaywebpage.html',d1)

    return render(request,'retrievedata.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}

    return render(request,'checkbox.html',d)


def radiobutton(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'radiobutton.html',d)