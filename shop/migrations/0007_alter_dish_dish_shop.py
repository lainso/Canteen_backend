# Generated by Django 4.1.7 on 2024-03-19 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_alter_shop_shop_cus"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="dish_shop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="shop.shop"
            ),
        ),
    ]
