# Generated by Django 3.2.13 on 2022-12-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0009_achivements_contact_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
                ('page', models.CharField(choices=[('about', 'about'), ('faculty', 'faculty')], default='none', max_length=200)),
                ('about', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='mission',
            options={'verbose_name': 'Mission', 'verbose_name_plural': 'Missions'},
        ),
        migrations.AlterModelOptions(
            name='vission',
            options={'verbose_name': 'Vission', 'verbose_name_plural': ' Vission'},
        ),
    ]
