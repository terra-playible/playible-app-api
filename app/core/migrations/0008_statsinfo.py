# Generated by Django 3.2.7 on 2021-09-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210927_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=155)),
                ('key', models.CharField(max_length=155)),
                ('multiplier', models.DecimalField(decimal_places=2, max_digits=19)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
    ]