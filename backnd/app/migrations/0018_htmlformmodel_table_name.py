# Generated by Django 4.2.1 on 2023-06-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_htmlformmodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='htmlformmodel',
            name='table_name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]