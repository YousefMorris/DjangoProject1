# Generated by Django 4.2.9 on 2024-02-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0004_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="ecommerceapp/images/"
            ),
        ),
    ]