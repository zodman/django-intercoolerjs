# Generated by Django 2.2.1 on 2019-05-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190501_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]