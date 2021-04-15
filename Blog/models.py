from django.db import models
from django.contrib.auth.models import User



# Create your models here.
 
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()

class Profile(models.Model):
    phone = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload/profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'