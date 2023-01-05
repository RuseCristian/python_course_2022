from django.db import models


# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.city} -> {self.country}"


class Log(models.Model):

    action_choices = (('created', 'created'),
                      ('updated', 'updated'),
                      ('refresh', 'refresh')
                      )

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=action_choices)
    url = models.CharField(max_length=100)
