# Generated by Django 2.0.6 on 2018-06-21 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20180621_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='notes.Category'),
        ),
    ]
