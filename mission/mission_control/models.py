from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=120)
    week = models.IntegerField()
    DAY_CHOICES = (
        ("1", "Monday"),
        ("2", "Tuesday"),
        ("3", "Wednesday"),
        ("4", "Thursday"),
        ("5", "Friday"),
    )
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    AMPM_CHOICES = (
        ("AM", "AM"),
        ("PM", "PM"),
    )
    am_pm = models.CharField(max_length=10, choices=AMPM_CHOICES)


class Exercise(models.Model):
    name = models.CharField(max_length=120)
    topic = models.ForeignKey(Topic, related_name='exercise')
    difficulty = models.CharField(max_length=120)
