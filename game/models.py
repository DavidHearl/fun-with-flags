from django.db import models


class Flag(models.Model):
    flag = models.CharField(max_length=250)
    programatic_name = models.CharField(max_length=254, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    fact = models.TextField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    difficulty = models.DecimalField(max_digits=6, decimal_places=5, null=True, blank=True)

