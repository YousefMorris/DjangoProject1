# Generated by Django 4.2.9 on 2024-02-05 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0006_category_product_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="createdat",
        ),
        migrations.RemoveField(
            model_name="category",
            name="price",
        ),
        migrations.RemoveField(
            model_name="category",
            name="productimage",
        ),
        migrations.RemoveField(
            model_name="category",
            name="updatedat",
        ),
    ]
