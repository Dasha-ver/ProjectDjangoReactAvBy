# Generated by Django 5.0.6 on 2024-07-17 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('av_app', '0005_car_bookmakers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercarrelation',
            name='in_bookmarks',
        ),
    ]
