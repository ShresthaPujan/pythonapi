# Generated by Django 4.0.7 on 2022-09-07 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]