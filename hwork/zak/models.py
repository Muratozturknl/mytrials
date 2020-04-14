
from django.db import models
#from ckeditor.fields import RichTextField

# we are creating model for admin panel

class Zak(models.Model):
    child = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    # auto.User --> Allows us to retrieve user names from the specified table
   # on_delete -->  Deletes all data when the author name is deleted
    task = models.CharField(max_length = 50,)
    # The title and the total number of characters were created in the table.
    # The name was then customized to 'verbose name = başlık'.
    amount = models.FloatField()
    date = models.DateTimeField( auto_now_add = True)
    # The data column were created auto as Instant Current Time
    # The name was then customized to 'verbose name = oluşturulma zamanı'.
   

    def __str__(self):
        return self.task
    # We have customized the name of an object added here. 
    # The object name as Article object (1) will appear as title (başlık).
    


    # Note: 1-We will save the created Article model to admin.py page.
    # 2-We will continue to customize the admin panel in admin.py.


    # modeli admin panele kaydedeceğiz.

