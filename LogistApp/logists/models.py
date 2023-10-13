from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Vessels(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    photo = models.ImageField(default='img/ship/no-image.jpg', upload_to='img/ship')
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    IMO = models.PositiveIntegerField()
    name_in_en = models.CharField(max_length=300)
    latitude = models.CharField(max_length=100, default='0')
    longitude = models.CharField(max_length=100, default='0')
    icon = models.ImageField(default='img/icons/красный.png', upload_to='img/icons')


class Fuel(models.Model):
    vessels = models.OneToOneField(Vessels, on_delete=models.CASCADE, primary_key=True)
    b_r = models.CharField(max_length=50, default='0')
    b_b = models.CharField(max_length=50, default='0')
    b_c = models.CharField(max_length=50, default='0')
    N = models.CharField(max_length=50, default='0')
    Q = models.CharField(max_length=50, default='0')
    V = models.CharField(max_length=50, default='0')
    C = models.CharField(max_length=50, default='0')
    K = models.CharField(max_length=50, default='0')
    X = models.CharField(max_length=50, default='0')
    E = models.CharField(max_length=50, default='0')
