from django.db import models

# Create your models here.

class AboutFeature(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    is_featured = models.BooleanField()
    image_class = models.CharField(max_length=100)
    # id = models.IntegerField(primary_key=True)

    # def __init__(self, id, name, details, is_featured, image_class):
    #     self.id = id
    #     self.name = name
    #     self.details = details
    #     self.is_featured = is_featured
    #     self.image_class = image_class
