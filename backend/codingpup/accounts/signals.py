from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import User, Account

@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(pre_delete, sender=Account)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
