# Generated by Django 4.1.7 on 2023-03-01 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_user_birthday_user_location_user_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeoff',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
