# Generated by Django 3.2.11 on 2022-02-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0018_packaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='games'),
        ),
    ]