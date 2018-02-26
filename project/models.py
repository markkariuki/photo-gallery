from django.db import models
import datetime as dt


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
    image = models.ImageField(upload_to = 'photos/', null = True)
    image_name = models.CharField(max_length=30)
    image_descripton = models.TextField()
    location_taken = models.ForeignKey(location)
    image_category = models.ManyToManyField(categories)
    pub_date = models.DateTimeField(auto_now_add=True)



    @classmethod
    def todays_pictures(cls):
        today = dt.date.today()
        project = cls.objects.filter(pub_date__date=today)

        return pictures_today

    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(image_category__name__icontains=search_term)

        return pics
