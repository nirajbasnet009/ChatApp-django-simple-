# Generated by Django 4.2.11 on 2024-03-24 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.CharField(max_length=10000000)),
                (
                    "date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                ("room", models.CharField(max_length=1000)),
                ("user", models.CharField(max_length=100000)),
            ],
        ),
    ]