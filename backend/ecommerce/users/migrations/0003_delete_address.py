# Generated by Django 4.0.2 on 2022-03-16 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
