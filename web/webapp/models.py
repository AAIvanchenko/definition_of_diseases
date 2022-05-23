from django.db import models


# Create your models here.

# Create your models here.
class Images(models.Model):
    image = models.ImageField('Путь до изображения', db_index=True, upload_to='images')

    def __str__(self):
        return str(self.pk)
