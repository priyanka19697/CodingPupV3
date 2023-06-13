from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

from django.db.models.signals import post_save


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    phone = PhoneNumberField(blank=True, null=True)
    leetcode_link = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(upload_to="profile_pictures",blank=True, null=True)

    def __str__(self):
        return self.user.username

