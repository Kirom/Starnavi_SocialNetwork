from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class ExtendedUser(models.Model):
    """Extends basic user's model with last_activity field."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_extended_user(sender, instance, created, **kwargs):
    """Signal for creating new extended_user when basic user is created."""
    if created:
        ExtendedUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_extended_user(sender, instance, **kwargs):
    """Signal for saving new extended_user when basic user is created."""
    instance.extendeduser.save()


@receiver(post_delete, sender=User)
def delete_extended_user(sender, instance, **kwargs):
    """Signal for deleting extended_user when basic user is deleted."""
    if instance:
        ExtendedUser.objects.filter(user=instance).delete()
