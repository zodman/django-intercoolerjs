# Generated by Django 2.2.1 on 2019-05-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='name',
            field=models.CharField(help_text='Entry help text', max_length=30, unique=True),
        ),
    ]