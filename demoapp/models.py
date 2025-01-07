from django.db import models

# Create your models here.

class AboutFeature():
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    # id = models.IntegerField(primary_key=True)
    # is_featured = models.BooleanField()
    # image_class = models.CharField(max_length=100)

    # def __init__(self, id, name, details, is_featured, image_class):
    #     self.id = id
    #     self.name = name
    #     self.details = details
    #     self.is_featured = is_featured
    #     self.image_class = image_class
