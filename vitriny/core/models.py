from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    creation_date = models.DateField(auto_now_add=True)
    last_modification_date = models.DateField(auto_now=True)
    hidden = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/products',
                              max_length=200)
