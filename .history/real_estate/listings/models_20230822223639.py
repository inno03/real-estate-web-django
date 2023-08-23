from django.db import models


class Listing(models.model):
  title = models.CharField(max_length=150)
  price = models.IntegerField()
  num_bedrooms = models.IntegerField()
  