from django.db import models

# Create your models here.


class Transport(models.Model):
    name_auto = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=15, unique=True)
    uuid = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.name_auto}, {self.reg_number}'
