# Generated by Django 4.2.1 on 2023-06-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_user_type_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.CharField(max_length=200)),
            ],
        ),
    ]
