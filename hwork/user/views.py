from django.shortcuts import render,redirect
from .forms import RegisterForm , LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout

def register (request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid(): 
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            
            newUser= User(username= username)
            newUser.set_password(password)
            newUser.save()
            login(request, newUser)
            messages.success(request,"Saved...!")

            return redirect ("index")
        
        context = {
            "form": form
        }
        return render(request,"register.html", context)
    
    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request,"register.html", context)






def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        'form' : form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
       

        user = authenticate(username = username , password = password)
            # bir değişkene atama yaptık ve bu veriler databasede kayıtlımı diye sorgulanıyor.

        if user is None:
            messages.info(request, 'Invalid User Name / Password')
            return render(request, 'login.html', context)
                # giriş başarısız, tekrar login sayfasına döndürdü
     
        messages.success(request, username.capitalize()+', login successful')
            # if bloğuna girmedi yani giriş başarılı

        login(request, user)
            # user değişkenine atanan veriler ile login fonk. sayesinde giriş yapıldı

        return redirect('/zak/zakgeld')
            # giriş başarılı ana sayfaya yönlendiriliyor

    return render(request, 'login.html', context)
        # 54. stır ile aynı durum. bu bölümde if sorgusu b

def logoutUser (request):
    logout(request)
    messages.success (request,"Logged Out...!")
    
    return redirect("index")



def switch (request):
    logout(request)
    messages.success (request,"Logged Out...!")
    
    return redirect("/user/login")
