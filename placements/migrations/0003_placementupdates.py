# Generated by Django 3.2.13 on 2023-02-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0002_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('data', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
