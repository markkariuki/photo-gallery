from django.db import models

# Create your models here.
from django.db import models

class tags(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
