from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.TextField(null=True)
    street = models.TextField()
    zipcode= models.TextField()
    address = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return  self.user.username + " " +self.city + self.street + self.address