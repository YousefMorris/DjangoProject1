# Generated by Django 4.2.9 on 2024-02-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0003_remove_product_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
