# Generated by Django 3.2.11 on 2022-02-14 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]