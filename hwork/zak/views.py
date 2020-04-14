from django.shortcuts import render, redirect, get_object_or_404
from django .contrib import messages
from .forms import ZakForm
from .models import Zak
from django.contrib.auth.decorators import login_required
from django.http import request



# Create your views here.

def index (request):
    return render(request,"index.html")


@login_required(login_url = "user:login")
def addzak (request):
    form = ZakForm(request.POST or None)
    if form.is_valid():
        zak = form.save(commit=False)    
        zak.child = request.user
        zak.save()

        messages.success(request,"Saved!!")
        return redirect("index")
    return render(request,"addzak.html", {"form":form})

@login_required(login_url = "user:login")
def dashboard(request):
    zaks = Zak.objects.filter(child = request.user)
    context = {
        "zaks":zaks,
     
    }
    return render(request,"dashboard.html",context)   
    
@login_required(login_url = "user:login")
def update(request,id):

    zak = get_object_or_404(Zak,id = id)
    form = ZakForm(request.POST or None,instance = zak)
    if form.is_valid():
        zak = form.save(commit=False) 
        zak.child = request.user
        zak.save()
        messages.success(request," Updated!")
        return redirect("zak:dashboard")
    return render(request,"update.html",{"form":form})


@login_required(login_url = "user:login")
def delete(request,id):
    zak = get_object_or_404(Zak,id = id)

    zak.delete()

    messages.success(request,"Deleted!")

    return redirect("zak:dashboard")



def zaks(request):
    zaks = Zak.objects.all()


    
    return render(request,"zaks.html",{"zaks":zaks})