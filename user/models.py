from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70,blank=True)
    message = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)

    class Meta:
        db_table='user_info'

class SubscribeUser(models.Model):
    sub_email = models.EmailField(max_length=70,blank=True)

    class Meta:
        db_table='subscribe_user_info'


