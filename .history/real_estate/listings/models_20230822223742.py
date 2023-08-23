from django.db import models


class Listing(models.model):
  title = models.CharField(max_length=150)
  price = models.IntegerField()
  num_bedrooms = models.IntegerField()
  num_bathrooms = models.IntegerField()
  square_footage = models.IntegerField()
  address = models.CharField