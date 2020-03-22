# Create your views here.
from .models import Music,Contact
from django.shortcuts import render
from math import ceil


allmusic = []
def music(request):
    music = Music.objects.all()
    n = len(music)
    nSlides = n//4 + ceil((n//4) - (n/4))
    params = {'music':music,'range':range(1,nSlides),'nSlide':nSlides}
    return render(request,'music/music.html',params)


def home(request):
    music = Music.objects.all()
    n = len(music)
    active = n / 2
    params1 = {'music':music,'range':range(1,n),'active':active}
    return render(request,'music/home.html',params1)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(Name=name,Email=email,Phone=phone,desc=desc)
        contact.save()

    return render(request,'music/contact.html')


def musicView(request,myid):

    music = Music.objects.filter(id=myid)
    return render(request,'music/musicview.html',{"music":music[0]})

# About page for telling about 'Who we are?'--
def about(request):
    return render(request,'music/about.html')






