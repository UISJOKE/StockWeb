from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    article = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    photo = models.ImageField()
    description = models.CharField(max_length=1000)
    country = models.CharField(max_length=50)
    net_weight = models.FloatField()
    gross_weight = models.FloatField()
    price = models.FloatField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'