from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
