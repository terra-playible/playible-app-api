# Generated by Django 3.2.7 on 2022-01-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0005_game_gameasset_gameathlete_gameathletestat_gameschedule_gameteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='prize',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
            preserve_default=False,
        ),
    ]