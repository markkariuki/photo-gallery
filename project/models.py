from django.db import models

# Create your models here.

class location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class photos(models.Model):
    image = models.ImageField(upload_to = 'photos/', blank = True)
    image_name = models.CharField(max_length=30)
    image_descripton = models.TextField()
    location_taken = models.ForeignKey(location)
    image_category = models.ManyToManyField(categories)
