from django.db import models

# Create your models here.
class photos(models.Model):
    image = models.ImageField(upload_to = 'photos/', blank = True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location_taken = models.ForeignKey(Location)
    category = models.ManyToManyField(categories)
