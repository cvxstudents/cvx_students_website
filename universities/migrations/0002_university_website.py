# Generated by Django 3.2.12 on 2023-04-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='website',
            field=models.URLField(default='https://www.youtube.com/'),
        ),
    ]