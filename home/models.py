from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Tournament(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    t_id = models.CharField(max_length=50, blank=False)
    t_type = models.CharField(max_length=50, blank=False)
    t_cat = models.CharField(max_length=50, blank=False)
    max_player =  models.IntegerField(default=0)
    total_player = models.IntegerField(default=0)
    avl_player = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=50)
    link = models.URLField(max_length=150)
    match_time = models.DateTimeField()
    dt = models.DateTimeField(default=now)

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    t_id = models.CharField(max_length=50, blank=False)
    pubg_id = models.CharField(max_length=50, blank=False)
    position = models.IntegerField(default=0)
    kill = models.IntegerField(default=0)
    total_earn = models.FloatField(default=0)
    dt = models.DateTimeField(default=now)