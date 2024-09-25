# Generated by Django 5.0.6 on 2024-06-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("color", models.CharField(max_length=255)),
                ("price", models.FloatField()),
                ("stock", models.IntegerField()),
            ],
        ),
    ]
