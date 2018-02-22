from django.test import TestCase
import datetime as dt
from .models import photos, categories


class photosTestClass(TestCase):
    def setUp(self):
        self.photo = photos(image='imageurl', name='davy', descripton='kind')

    def test_photo_instance(self):
        self.assertTrue(isinstance(self.photo, photos))

    def test_save_photo_method(self):
        self.photo.save_image()
        photos = photos.objects.all()
        self.assertTrue(len(photos)>0)

    def test_delete_photo_method(self):
        self.photo.save_image()
        photos = photos.objects.all()
        self.photo.delete_image()
        photos = photos.objects.all()
        self.assertTrue(len(photos)==0)
