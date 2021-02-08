from django.db import models

# Create your models here.
class meme(models.Model):
    name=models.CharField(max_length=60)
    caption=models.CharField(max_length=100)
    url= models.URLField(max_length=250)

    def __str__(self):
        return 'meme'+str(self.id)
