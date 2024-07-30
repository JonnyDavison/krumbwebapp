from django.db import models

# Create your models here.
class Gallery(models.Model):
    """ Category model """

    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
