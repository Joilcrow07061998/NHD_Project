from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    uuid = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()




@receiver(post_save, sender=User)
def create_worker_profile(sender, instance, created, **kwargs):
    if created:
        Worker.objects.create(user=instance)

