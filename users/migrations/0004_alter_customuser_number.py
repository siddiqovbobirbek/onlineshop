# Generated by Django 4.1.3 on 2022-12-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='number',
            field=models.CharField(max_length=200),
        ),
    ]