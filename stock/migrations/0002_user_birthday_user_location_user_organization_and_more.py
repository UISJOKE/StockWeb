# Generated by Django 4.1.7 on 2023-03-01 11:13

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phone_field.models.PhoneField(default=1, max_length=31),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
