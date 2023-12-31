# Generated by Django 3.2.13 on 2023-02-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0003_placementupdates'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementTraning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='placement/training/')),
                ('data', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
