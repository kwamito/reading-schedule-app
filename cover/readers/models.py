from django.db import models
from django.utils import timezone
from .utils import PUBLICATION
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Reader(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image = models.ImageField(default='users.svg',upload_to='profile_image')
    date_joined = models.DateField(default=timezone.now)
    email = models.EmailField(default='not set')

    def get_absolute_url(self):
        return reverse('reader-detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.name.username
    

class Reading(models.Model):
    reader = models.ForeignKey(Reader,on_delete=models.PROTECT)
    date_reading = models.DateField(default=timezone.now)
    publication = models.CharField(max_length=30,choices=PUBLICATION,default='Needs to be set')
    title = models.CharField(max_length=120,default='Needs to be set')

    def get_absolute_url(self):
        return reverse('reading-detail', kwargs={'pk':self.pk})
    