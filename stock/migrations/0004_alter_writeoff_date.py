# Generated by Django 4.1.7 on 2023-03-01 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_writeoff_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeoff',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
