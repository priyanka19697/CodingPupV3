from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone = PhoneNumberField(blank=True)
    leetcode_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_pictures")
    
    def __str__(self):
        return self.user.username
    
def create_profile(sender, **kwargs):
    print(kwargs)
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
    
post_save.connect(create_profile, sender=User)
     
    

