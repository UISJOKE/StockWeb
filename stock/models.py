from django.db import models
from PIL import Image

from django.utils.safestring import mark_safe

class Stock(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    article = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='stock/pictures')
    description = models.CharField(max_length=1000)
    country = models.CharField(max_length=50)
    net_weight = models.FloatField()
    gross_weight = models.FloatField()
    price = models.FloatField()

    def save(self):
        super().save()
        img = Image.open(self.photo.path)

        output_size = (200, 200)
        img.thumbnail(output_size)
        name = self.photo.name
        img.save(name)

