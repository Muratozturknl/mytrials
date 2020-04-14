from django.contrib import admin
from .models import Zak
# Rester your models here.

@admin.register(Zak)
class ZakAdmin(admin.ModelAdmin):
  
   list_display = ('id','child', 'task',"amount",'date')
   
  
   class Meta:
      model= Zak


#admin.site.register(Zak,ZakAdmin)