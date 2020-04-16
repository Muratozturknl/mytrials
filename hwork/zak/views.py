from django.shortcuts import render, redirect, get_object_or_404
from django .contrib import messages
from .forms import ZakForm, PayForm
from .models import Zak
from django.contrib.auth.decorators import login_required
from django.http import request
from django.db.models import Sum, Avg


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
        return redirect("/zak/zakgeld")
    return render(request,"addzak.html", {"form":form})

@login_required(login_url = "user:login")
def dashboard(request):
    zaks = Zak.objects.filter(child = request.user).order_by("-date")
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


def zakgeld(request):
    zaks = Zak.objects.filter(child = request.user)
    toplam=Zak.objects.filter(child = request.user).aggregate(Sum('amount'))
    
    return render(request,"zakgeld.html",{"zaks":zaks,"toplam":toplam})   


def zaks(request):
    keyword = request.GET.get("keyword")

    if keyword:
        zaks = Zak.objects.filter(task__contains = keyword)
        return render(request,"zaks.html",{"zaks":zaks})
       
    zaks = Zak.objects.all().order_by("task")
    sum_geld=Zak.objects.aggregate(top=Sum('amount'))
    pay_geld=Zak.objects.filter(task="payment").aggregate(paid=Sum('amount'))
    
    remain_geld= "a"
    return render(request,"zaks.html",
    {"zaks":zaks, "sum_geld":sum_geld, "pay_geld":pay_geld,"remain_geld":remain_geld})
















@login_required(login_url = "user:login")
def payment (request):
    form = PayForm(request.POST or None)
    if form.is_valid():
        pay = form.save(commit=False)    
        pay.child = request.user
        pay.save()

        messages.success(request,"Payment Done!!")
        return redirect("/zak/zakgeld")
    return render(request,"payment.html", {"form":form})



