from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    article = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    photo = models.ImageField()
    description = models.CharField(max_length=1000)
    country = models.CharField(max_length=50)
    net_weight = models.FloatField()
    gross_weight = models.FloatField()
    price = models.FloatField()
    clien_price = models.FloatField(default= 0)
    count = models.PositiveIntegerField('Count in stock(item)', blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'