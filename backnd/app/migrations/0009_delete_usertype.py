# Generated by Django 4.2.1 on 2023-05-09 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_usertype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserType',
        ),
    ]