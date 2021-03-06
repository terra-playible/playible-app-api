# Generated by Django 3.2.7 on 2022-01-14 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_asset_unique_asset'),
        ('fantasy', '0004_auto_20220111_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=155)),
                ('start_datetime', models.DateTimeField()),
                ('duration', models.IntegerField()),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='GameAthlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('athlete', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.athlete')),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.game')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='GameTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=155)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.game')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='GameSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('datetime', models.DateTimeField()),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.game')),
                ('team1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='GameSchedule_team1', to='fantasy.team')),
                ('team2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='GameSchedule_team2', to='fantasy.team')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='GameAthleteStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('fantasy_score', models.DecimalField(decimal_places=2, max_digits=19)),
                ('game_athlete', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.gameathlete')),
                ('game_schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.gameschedule')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='GameAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.asset')),
                ('game_athlete', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.gameathlete')),
                ('game_team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fantasy.gameteam')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
    ]
