# Generated by Django 5.0.6 on 2024-06-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('av_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.FloatField(default=3.2),
        ),
    ]
