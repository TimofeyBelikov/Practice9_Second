from django.db import models

class Car( models.Model):
    color = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    car_model = models.CharField(max_length=100)
    def __str__(self):
        return self.type+"_"+self.car_model

class Boat(models.Model):
    boat_model = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    weight = models.IntegerField()
    def __str__(self):
        return self.boat_model+"_"+self.engine