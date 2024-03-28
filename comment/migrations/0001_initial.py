# Generated by Django 4.1.7 on 2023-10-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notifications",
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
                ("noti_title", models.CharField(max_length=50)),
                ("noti_content", models.TextField()),
                ("noti_sendtime", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("pay_num", models.CharField(max_length=25)),
                ("pay_time", models.CharField(max_length=25)),
                ("pay_money", models.DecimalField(decimal_places=2, max_digits=10)),
                ("pay_way", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Promotions",
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
                ("promo_name", models.CharField(max_length=100)),
                ("promo_des", models.TextField()),
                ("promo_start", models.CharField(max_length=25)),
                ("promo_end", models.CharField(max_length=25)),
            ],
        ),
    ]