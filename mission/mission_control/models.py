from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=120)
    week = models.CharField(max_length=120)
    day = models.CharField(max_length=120)
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

