from django.shortcuts import render,redirect
from .models import Zakgeld
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Sum, Count


# Create your views here.


def index(request):
   return render(request,"index.html")


def minizakgeld_add (request):
    if request.method == "POST":
        person = request.POST['person']
        task = request.POST['task']
        amount = request.POST['amount']

        minizakgeld=Zakgeld(person=person, task=task, amount=amount)
        minizakgeld.save()

        return redirect('/')
    
    return render(request, "minizakgeld_add.html")



def minizakgeld_details (request):
    da=Zakgeld.objects.all().order_by("id")
    
    context = {
        "da": da    }
    return render(request,"minizakgeld_details.html", context)


def child_1(request):
    Zakgelds=Zakgeld.objects.filter(person="feridihsan").order_by('-date')
    
    context = {
        "Zakgelds": Zakgelds
    }
    
    return render(request, "child_1.html",context )


def child_2(request):
    Zakgelds=Zakgeld.objects.filter(person="ahmedvedat").order_by('amount')
    
    context = {
        "Zakgelds": Zakgelds
    }
    
    return render(request, "child_2.html",context )


def child_3 (request):
    Zakgelds=Zakgeld.objects.filter(person="alisami").order_by('-amount')
    
    context = {
        "Zakgelds": Zakgelds
    }
    
    return render(request, "child_3.html",context )











def toplam (request):
    toplam=Zakgeld.objects.all()
    
    context = { "toplam": toplam }
    print(toplam)
    


