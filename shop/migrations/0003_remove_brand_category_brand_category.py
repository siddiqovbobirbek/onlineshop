# Generated by Django 4.1.2 on 2022-11-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category',
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ManyToManyField(to='shop.category'),
        ),
    ]