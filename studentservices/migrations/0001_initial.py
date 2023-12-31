# Generated by Django 3.2.13 on 2023-02-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtsEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='arts/events')),
            ],
        ),
        migrations.CreateModel(
            name='ArtsGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='arts/gallery')),
            ],
        ),
        migrations.CreateModel(
            name='artsTeamStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(choices=[('cetus', 'cetus'), ('pegasus', 'pegasus'), ('taurs', 'taurs'), ('lupus', 'lupus')], max_length=100)),
                ('logo', models.ImageField(default='arts/teams/logos/default.png', upload_to='arts/teams/logos')),
                ('score', models.IntegerField(default=0)),
                ('won', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
                ('color', models.CharField(default='red-700', max_length=100)),
                ('image', models.ImageField(upload_to='arts/teams')),
            ],
        ),
        migrations.CreateModel(
            name='Artsupdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('data', models.TextField(default='No data')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='clubs/logos')),
                ('description', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IICCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='iic/certificates')),
            ],
        ),
        migrations.CreateModel(
            name='IICCommitee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('member_type', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('designamtion', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NssEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='nss/events')),
            ],
        ),
        migrations.CreateModel(
            name='NssGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='nss/gallery')),
            ],
        ),
        migrations.CreateModel(
            name='NssStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='nss/students')),
            ],
        ),
        migrations.CreateModel(
            name='SportsEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='sports/events')),
            ],
        ),
        migrations.CreateModel(
            name='SportsGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='arts/gallery')),
            ],
        ),
        migrations.CreateModel(
            name='SportsTeamStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(choices=[('cetus', 'cetus'), ('pegasus', 'pegasus'), ('taurs', 'taurs'), ('lupus', 'lupus')], max_length=100)),
                ('logo', models.ImageField(default='sports/teams/logos/default.png', upload_to='sports/teams/logos')),
                ('score', models.IntegerField(default=0)),
                ('won', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
                ('color', models.CharField(default='red-700', max_length=100)),
                ('image', models.ImageField(upload_to='sports/teams')),
            ],
        ),
        migrations.CreateModel(
            name='SportsUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('data', models.TextField(default='No data')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UnionCommitee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='union/member', verbose_name='Member Image')),
                ('position', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='WomenCellCommitee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('department', models.CharField(max_length=300)),
                ('designamtion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='NssFaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.ManyToManyField(to='website.Faculty')),
            ],
        ),
    ]
