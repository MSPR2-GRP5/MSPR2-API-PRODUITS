# Generated by Django 5.0.6 on 2024-06-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PRODUITS", "0002_products_stocks"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="description",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
