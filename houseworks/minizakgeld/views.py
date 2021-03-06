from django.shortcuts import render,redirect, HttpResponse
from .models import Zakgeld
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Sum, Count


# Create your views here.


def index(request):
   return render(request,"index.html")


def minizakgeld_add (request):
    if request.method == "POST":
        child = request.POST['child']
        task = request.POST['task']
        amount = request.POST['amount']

        minizakgeld=Zakgeld(child=child, task=task, amount=amount)
        minizakgeld.save()

        return redirect('/')
    
    return render(request, "minizakgeld_add.html")


#şkşldşadjaşdjaşdk

def detail (request,id):
    return HttpResponse("Detail:" + str(id))




def minizakgeld_details (request):
    da=Zakgeld.objects.all()
       
    context = {
        "da": da 
            }
    return render(request,"minizakgeld_details.html", context)







def child_1(request):
    Zakgelds=Zakgeld.objects.filter(child="feridihsan").order_by('-date_created')
    toplam_amount = toplam("feridihsan")
    context = {
        "Zakgelds": Zakgelds,
        "toplam":toplam_amount
    }
    
    return render(request, "child_1.html",context )


def child_2(request):
    Zakgelds=Zakgeld.objects.filter(child="ahmedvedat").order_by('amount')
    toplam_amount = toplam("ahmedvedat")
    context = {
        "Zakgelds": Zakgelds,
        "toplam":toplam_amount    }
    
    return render(request, "child_2.html",context )


def child_3 (request):
    Zakgelds=Zakgeld.objects.filter(child="alisami").order_by('-amount')
    
    toplam_amount = toplam("alisami")

    context = {
        "Zakgelds": Zakgelds,
        "toplam":toplam_amount
    }   
    return render(request, "child_3.html",context )

def toplam (name):
    
    all_objects_child = Zakgeld.objects.filter(child=name)
    toplam = 0

    for i in range(len(all_objects_child)):
        toplam += all_objects_child[i].amount

    return toplam   


