from django.contrib import admin
from django.urls import path, include
from .import views


app_name="zak"


urlpatterns = [
    path('dashboard/',views.dashboard, name = "dashboard"),
    path('addzak/', views.addzak, name="addzak"),
    path('update/<int:id>',views.update,name = "update"),
    path('delete/<int:id>',views.delete,name = "delete"),
    path('zaks/',views.zaks,name = "zaks"),
    path('zakgeld/',views.zakgeld,name = "zakgeld"),
    path('payment/', views.payment, name="payment"),

]
