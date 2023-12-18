from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    datetime = models.DateTimeField()

    def __str__(self):
        return str(self.datetime)
