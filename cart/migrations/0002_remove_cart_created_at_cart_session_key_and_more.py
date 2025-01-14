# Generated by Django 4.2 on 2024-07-17 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="created_at",
        ),
        migrations.AddField(
            model_name="cart",
            name="session_key",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
