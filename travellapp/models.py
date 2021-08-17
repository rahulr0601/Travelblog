from django.db import models
# Create your models here.


class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class blog(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='blog-picture')
    desc = models.TextField()
    date = models.DateField()
