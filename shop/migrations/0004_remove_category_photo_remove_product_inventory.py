# Generated by Django 4.2 on 2024-06-14 14:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_product_brand"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="photo",
        ),
        migrations.RemoveField(
            model_name="product",
            name="inventory",
        ),
    ]