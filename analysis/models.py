from django.db import models

# Create your models here.
 
class ICU_Beds(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pin_code = models.IntegerField(default=0)
    hospital = models.CharField(max_length=100)
    address_link = models.CharField(max_length=700, default="abc")
    

    def __str__(self):
        return self.state

class Beds(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pin_code = models.IntegerField(default=0)
    hospital = models.CharField(max_length=100)
    address_link = models.CharField(max_length=700 , default="abc")
    
    def __str__(self):
        return self.state

class Ambulance(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pin_code = models.IntegerField(default=0)
    hospital = models.CharField(max_length=100)
    address_link = models.CharField(max_length=700 , default="abc")

    
    def __str__(self):
        return self.state

class Vaccination(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pin_code = models.IntegerField(default=0)
    centre = models.CharField(max_length=100)
    address_link = models.CharField(max_length=700 , default="abc")
    
    def __str__(self):
        return self.state

class Plasma(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pin_code = models.IntegerField(default=0)
    hospital = models.CharField(max_length=100)
    address_link = models.CharField(max_length=700 , default="abc")
    
    def __str__(self):
        return self.state

class Oxygen(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pin_code = models.IntegerField(default=0)
    hospital = models.CharField(max_length=100)
    address_link = models.CharField(max_length=700 , default="abc")
    
    def __str__(self):
        return self.state

class Patient_Status(models.Model):
    cured = models.IntegerField(default=1)
    death = models.IntegerField(default=1)
    admitted = models.IntegerField(default=1)
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.state
