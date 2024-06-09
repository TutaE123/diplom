from django.conf import settings
from django.db import models
from django.utils import timezone

    

class Car (models.Model):
    title = models.CharField(max_length=200)
    example = models.TextField()
     
    def __str__(self) :
        return self.title
    
class Status (models.Model):
    title = models.CharField(max_length=200)
     
    def __str__(self) :
        return self.title
    

class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='1')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place_start = models.CharField(max_length=200)
    place_end = models.CharField(max_length=200)
    tariff = models.TextField(default='Уточняется')
    numder = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.place_end} + {self.date}'

