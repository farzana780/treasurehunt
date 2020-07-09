from django.db import models

# Create your models here.
class treasureGram(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    material = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    image_url = models.CharField(max_length=400)

    def __str__(self):
        return self.name