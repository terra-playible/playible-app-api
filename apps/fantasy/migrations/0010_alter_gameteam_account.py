# Generated by Django 3.2.11 on 2022-02-14 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0001_initial'),
        ('fantasy', '0009_auto_20220214_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameteam',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_account.account'),
        ),
    ]