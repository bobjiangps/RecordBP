# Generated by Django 3.0.8 on 2020-08-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0009_person_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='expose',
            field=models.BooleanField(default=False, verbose_name='是否曝光'),
        ),
    ]
