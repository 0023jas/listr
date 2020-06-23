from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoItem(models.Model):
    userName = models.TextField()
    content = models.TextField()

class CurrentlyWorkingItem(models.Model):
    userName = models.TextField()
    contentCW = models.TextField()

class FinishedItem(models.Model):
    userName = models.TextField()
    contentDone = models.TextField()

"""
#Auto create UserData table when user signs up 
from django.dispatch import receiver
from django.db.models.signals import post_save
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        TodoItem.objects.create( userName = instance )"""