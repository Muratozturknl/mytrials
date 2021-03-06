from django.shortcuts import render, redirect, get_object_or_404
from django .contrib import messages
from .forms import ZakForm, PayForm
from .models import Zak
from django.contrib.auth.decorators import login_required
from django.http import request
from django.db.models import Sum, Avg, Q
from collections import Counter


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
def payment (request):
    initial_data= {
        "task": "*payment*"
    }
    form = PayForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        pay = form.save(commit=False)    
        pay.child = request.user
        pay.save()

        messages.success(request,"Payment Done!!")
        return redirect("/zak/zakgeld") 
    return render(request,"payment.html", {"form":form})

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
    context={ "form":form }
    return render(request,"update.html",context)


@login_required(login_url = "user:login")
def delete(request,id):
    zak = get_object_or_404(Zak,id = id)

    zak.delete()

    messages.success(request,"Deleted!")

    return redirect("zak:dashboard")

""" ............................................................................................................
.............................................................................................."""


@login_required(login_url = "user:login")
def dashboard(request):
    a=zaks.filter(~Q(task= "*payment*"))
    b=a.aggregate(Earned=Sum('amount'))
    sum_geld = int(b["Earned"])

    c=zaks.filter(task= "*payment*")
    d=c.aggregate(Paid=Sum('amount'))
    pay_geld = int(d["Paid"])
    
    remain_geld=sum_geld-pay_geld
    context={

        "zaks":zaks, 
        "sum_geld":sum_geld, 
        "pay_geld":pay_geld,
        "remain_geld":remain_geld

    }
    return render(request,"dashboard.html",context)   


def zaks(request):
    keyword = request.GET.get("keyword")

    if keyword:
        zaks = Zak.objects.filter(task__contains = keyword)
        context= { "zaks":zaks }
        
        return render(request,"zaks.html", context)
       
    zaks = Zak.objects.all().order_by("task")
    a=zaks.filter(~Q(task= "*payment*"))
    b=a.aggregate(Earned=Sum('amount'))
    sum_geld = int(b["Earned"])

    c=zaks.filter(task= "*payment*")
    d=c.aggregate(Paid=Sum('amount'))
    pay_geld = int(d["Paid"])

    remain_geld=sum_geld-pay_geld
    context={

        "zaks":zaks, 
        "sum_geld":sum_geld, 
        "pay_geld":pay_geld,
        "remain_geld":remain_geld

    }
    return render(request,"zaks.html", context)



def zakgeld(request):
    zaks = Zak.objects.filter(child = request.user)  

    a=zaks.filter(~Q(task= "*payment*"))
    b=a.aggregate(Earned=Sum('amount'))
    sum_geld = int(b["Earned"])

    c=zaks.filter(task= "*payment*")
    d=c.aggregate(Paid=Sum('amount'))
    pay_geld = int(d["Paid"])
    
    remain_geld=sum_geld-pay_geld
    
    context={

        "zaks":zaks, 
        "sum_geld":sum_geld, 
        "pay_geld":pay_geld,
        "remain_geld":remain_geld

    }

    return render(request,"zakgeld.html",context)
