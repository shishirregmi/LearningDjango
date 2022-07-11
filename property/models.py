from pyexpat import model
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

from agent.models import Agent

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length = 200)
    longDesc = models.CharField(max_length = 200)
    shortDesc = models.CharField(max_length = 200)
    roadInFront = models.BooleanField(default=False)
    distanceFromHighway = models.IntegerField(default=0)
    kitchen = models.IntegerField(default=0)
    bedroom = models.IntegerField(default=0)
    hall = models.IntegerField(default=0)
    garage = models.BooleanField(default=False)
    area = models.CharField(max_length = 200)
    price = models.CharField(max_length = 200)
    cardImage = models.ImageField(upload_to="media/images/cardImages", null=True)
    coverImage = models.ImageField(upload_to="media/images/coverImages", null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    featured = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title