from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class BusinessUnit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    jury = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    application_start_time = models.DateTimeField(null=True)
    application_end_time = models.DateTimeField(null=True)

    coordinator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    business_unit = models.OneToOneField(
        BusinessUnit, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default_program.png', upload_to='images/program_images')

    def __str__(self):
        return self.name

    class Meta:
        ordering =['-updated', '-created']