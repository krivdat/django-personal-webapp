from django.db import models
import random

class Adjective1(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def rnd(self):
        return word.objects.order_by('?').first()

    def __str__(self):
        return self.name
