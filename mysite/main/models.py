from django.db import models

# Create your models here.
class Phons(models.Model):

    name = models.CharField('Phone name',max_length=50)

    def __str__(self):
        return self.name