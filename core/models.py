from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)