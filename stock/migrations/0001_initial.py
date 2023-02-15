# Generated by Django 4.1.7 on 2023-02-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to='stock/pictures')),
                ('description', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=50)),
                ('net_weight', models.FloatField()),
                ('gross_weight', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
    ]