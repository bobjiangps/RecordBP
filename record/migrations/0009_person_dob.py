# Generated by Django 3.0.8 on 2020-07-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0008_auto_20200706_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name="出生日期"),
        ),
    ]
