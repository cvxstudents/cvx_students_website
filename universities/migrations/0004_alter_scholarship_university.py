# Generated by Django 3.2.12 on 2023-04-28 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0003_university_programmes_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.university'),
        ),
    ]