# Generated by Django 4.1.3 on 2022-12-05 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_productphoto_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productphoto',
            name='url',
        ),
    ]
