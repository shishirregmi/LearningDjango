from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    profile_pic = models.ImageField(upload_to="images/profileImages/", null=True)
    
    def __str__(self):
        return self.name
