from django.db import models
from datetime import datetime
from django.db.models import FloatField

# Create your models here.

class Zakgeld(models.Model):
    child  = models.CharField(max_length=200)
    task    = models.TextField()
    amount  = models.FloatField()   
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.child