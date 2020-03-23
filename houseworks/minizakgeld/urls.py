from django.urls import path, include
from .import views

urlpatterns = [
    path ('', views.index, name="index"),
    path('minizakgeld_details', views.minizakgeld_details, name="minizakgeld_details"),
    path('minizakgeld_add', views.minizakgeld_add, name="minizakgeld_add"),
    path('child_1', views.child_1, name="child_1"),
    path('child_2', views.child_2, name="child_2"),
    path('child_3', views.child_3, name="child_3"),
    path('toplam', views.toplam, name="toplam"),
]

