# Generated by Django 4.2.1 on 2023-06-11 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_user_type_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_type',
        ),
    ]
