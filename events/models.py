from django.db import models
from django.urls import reverse

from users.models import User

# Create your models here.
""" EVENT MODEL / EVENT TABLE """
class Event(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250,blank=True,null=True)
    date = models.DateField()
    time = models.TimeField()
    phone_number = models.CharField(max_length=10)
    price = models.PositiveIntegerField(default=0)
    organizer = models.CharField(max_length=250)
    cover = models.ImageField(upload_to='events/')
    description = models.TextField()
    featured = models.BooleanField(default=False)
    user = models.ForeignKey(User,related_name='events',on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id',]
    
    @property
    def get_absolute_url(self):
        return reverse('event-detail',args=[self.pk])

""" APPLICATION / EVENT APPLICATION TABLE """
class Application(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='applications')
    user  = models.ForeignKey(User,on_delete=models.CASCADE,related_name='applications')
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.name
    
    class Meta:
        ordering = ['-id',]