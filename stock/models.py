import datetime

from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(default='default.png')
    organization = models.CharField(max_length=50)
    location = models.CharField(max_length=15)
    phone = PhoneField()
    birthday = models.CharField(max_length=10)


class Provider(models.Model):
    contact = models.CharField(max_length=500)
    adress = models.CharField(null=False, blank=False, max_length=500)
    contact_number = PhoneField(null=False, blank=False, unique=True)
    Requisites = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.contact


class Stock(models.Model):
    article = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=150)
    photo = models.ImageField(blank=True, default='default.png')
    description = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)
    net_weight = models.FloatField(null=True, blank=True)
    gross_weight = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    client_price = models.FloatField(default=0, editable=False, blank=True)
    count = models.PositiveIntegerField('Count in stock(item)', blank=True, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.article + ' ' + self.name

    def save(self, *args, **kwargs):
        self.client_price = self.price * 1.3
        super().save(*args, **kwargs)


class Buyer(models.Model):
    ESSENCE = (
        ('legal entity', 'Юр.Лицо'),
        ('Individual entity', 'Физ.Лицо'),
    )
    ESSENCE = models.CharField(choices=ESSENCE, max_length=500)
    contact = models.CharField(max_length=500)
    adress = models.CharField(null=False, blank=False, max_length=500)
    contact_number = PhoneField(null=False, blank=False, unique=True)
    Requisites = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.contact


class WriteOff(models.Model):
    ACTION_CHOICES = (
        ('write-off', 'Списание'),
        ('sell', 'Продажа'),
        ('stocktaking', 'Инвентаризация')
    )
    article = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today,blank=True)
    action = models.CharField(choices=ACTION_CHOICES, max_length=500)
    contact = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    count = models.PositiveIntegerField(null=False, blank=False, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.article.count == 0:
            self.count = 0
        self.article.count -= self.count
        self.article.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return '№WF' + str(self.id) + ' ' + str(self.date)


class Procurement(models.Model):
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    price_on_client = models.DecimalField(blank=True, editable=False, decimal_places=2, max_digits=100)
    datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.price_on_client = self.price * 1.3
        if self.item.price < self.price:
            self.item.price = self.price
            self.item.clien_price = self.price_on_client
        self.item.count += self.count
        self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return '№P' + str(self.id) + ' ' + self.item.name + ' ' + str(self.datetime)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
