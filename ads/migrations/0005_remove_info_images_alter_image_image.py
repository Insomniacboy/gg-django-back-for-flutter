# Generated by Django 4.0.3 on 2022-03-25 09:01

import ads.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_info_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='images',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=ads.models.path_and_rename),
        ),
    ]
