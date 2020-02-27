from distutils.text_file import TextFile
from numbers import Integral

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)

#     def __str__(self):
#         return self.username


class Game_type(models.Model):
    game_type_id = models.CharField(max_length=255, primary_key=True)
    type_name = models.CharField(max_length=255)


class Game(models.Model):
    game_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    game_type_id = models.ForeignKey(Game_type, on_delete=models.PROTECT)
    developer = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    price = models.IntegerField()


class User_games(models.Model):
    user_game_id = models.CharField(max_length=255, primary_key=True)
    purchased_date = models.DateTimeField()
    serial = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)


class Image(models.Model):
    lmage_id = models.CharField(max_length=255, primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)
    image_url = models.CharField(max_length=255)