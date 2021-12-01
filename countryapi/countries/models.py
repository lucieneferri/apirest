from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    carea = models. IntegerField(help_text='(in square kilometers)')

    
