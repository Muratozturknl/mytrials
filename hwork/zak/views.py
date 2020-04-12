from django.shortcuts import render, redirect, get_object_or_404
from django .contrib import messages
from .models import Zak
from django.contrib.auth.decorators import login_required
# Create your views here.

def index (request):
    return render(request,"index.html")


def dashboard(request):
    Zaks = Zak.objects.filter(child = request.user)
    context = {
        "Zaks":Zaks
    }
    return render(request,"dashboard.html",context)