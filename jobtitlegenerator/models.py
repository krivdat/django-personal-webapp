from django.db import models


class Adjective1(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word

class Adjective2(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word

class Adjective3(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word

class Position(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word
