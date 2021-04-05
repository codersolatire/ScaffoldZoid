from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.IntegerField(primary_key='True')
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    user_type = models.CharField(max_length=5)
    email_id = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    profile_picture = models.FileField(
        upload_to="static/uploads/", null="True")


class Oranges(models.Model):
    orange_id = models.IntegerField(primary_key='True')
    user_id = models.IntegerField()
    orange_type = models.CharField(max_length=150)
    rate = models.CharField(max_length=5)
