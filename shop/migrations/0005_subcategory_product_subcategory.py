# Generated by Django 4.2 on 2024-07-22 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_remove_category_photo_remove_product_inventory"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subcategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="shop.subcategory",
            ),
        ),
    ]
