from django.db import models
import datetime


class product(models.Model):
    image=models.ImageField(null=False,blank=False)
    name=models.CharField(max_length=40,null=False,blank=False)
    price=models.FloatField()
    is_published=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime,blank=True)
    def __str__(self):
        return self.name

# Create your models here.
