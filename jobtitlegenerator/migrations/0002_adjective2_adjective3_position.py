# Generated by Django 2.0.6 on 2018-07-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobtitlegenerator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjective2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adjective3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
