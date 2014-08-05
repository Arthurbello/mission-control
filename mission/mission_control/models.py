from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=120)
    DAY_CHOICES = (
        ("1", "Monday"),
        ("2", "Tuesday"),
        ("3", "Wednesday"),
        ("4", "Thursday"),
        ("5", "Friday"),
    )
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    week = models.CharField(max_length=120)
    AMPM_CHOICES = (
        ("AM", "AM"),
        ("PM", "PM"),
    )
    am_pm = models.CharField(max_length=10, choices=AMPM_CHOICES)


class Exercise(models.Model):
    name = models.CharField(max_length=120)
    topic = models.ForeignKey(Topic, related_name='exercise')
    # maybe set as a choice instead?
    difficulty = models.CharField(max_length=120)
