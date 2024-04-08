from django.db import models



# Create your models here.
class Locations(models.Model):
    name = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    lat = models.CharField(max_length=200,blank=True, null=True)
    lng = models.CharField(max_length=200,blank=True, null=True)
    place_id = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.name
    


class driver(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20)
    car_registration = models.CharField(max_length=20)
    car_make = models.CharField(max_length=100)
    # Replace image_url with ImageField
    image = models.ImageField(upload_to='driver_images', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


   


    
