from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Add additional fields as needed
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField(auto_now_add=True)
    points = models.IntegerField(default=0)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    activity_type = models.CharField(max_length=50)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    week = models.DateField()
