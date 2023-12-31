# Generated by Django 3.2.13 on 2023-01-04 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0018_newsletters_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='associations',
            name='short_description',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='professionalbodies',
            name='short_description',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='associations',
            name='data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='professionalbodies',
            name='data',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='AssociationTeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='Association')),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
                ('assosiation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.associations')),
            ],
        ),
        migrations.CreateModel(
            name='AssociationsEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150)),
                ('short_description', models.CharField(default='None', max_length=500)),
                ('image', models.ImageField(upload_to='AssociationsImagesEvents')),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
                ('assosiation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.associations')),
            ],
        ),
    ]
