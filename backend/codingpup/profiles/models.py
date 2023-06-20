from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

from django.db.models.signals import post_save


#  in frontend when there is a delete Profile button - call should be made to delete user endpoint

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default="", null=True, blank=True)
    city = models.CharField(max_length=100, default="", null=True, blank=True)
    phone = PhoneNumberField(blank=True, default="", null=True)
    leetcode_link = models.CharField(max_length=100,blank=True, default="", null=True)
    image = models.ImageField(upload_to="profile_pictures",blank=True, default=None, null=True)

    def __str__(self):
        return self.user.username

