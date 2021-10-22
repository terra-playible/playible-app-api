# Generated by Django 3.2.7 on 2021-10-22 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fantasy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('username', models.CharField(max_length=155)),
                ('wallet_addr', models.CharField(max_length=155, unique=True)),
                ('image_url', models.CharField(blank=True, max_length=155, null=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='AssetProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=155)),
                ('value', models.CharField(max_length=155)),
                ('data_type', models.CharField(choices=[('NUMBER', 'Number'), ('STRING', 'String')], default='STRING', max_length=30)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='PrelaunchEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='AssetContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('symbol', models.CharField(max_length=155, unique=True)),
                ('name', models.CharField(max_length=155)),
                ('contract_addr', models.CharField(max_length=155)),
                ('athlete_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasy.athlete')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=155)),
                ('image_url', models.CharField(blank=True, max_length=155, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.assetcontract')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
    ]
