# Generated by Django 4.2.9 on 2024-02-04 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0005_alter_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
                (
                    "productimage",
                    models.ImageField(
                        blank=True, null=True, upload_to="ecommerceapp/images/"
                    ),
                ),
                (
                    "categoryimage",
                    models.ImageField(
                        blank=True, null=True, upload_to="ecommerceapp/images/"
                    ),
                ),
                ("price", models.IntegerField(default=0)),
                ("createdat", models.DateTimeField(auto_now_add=True)),
                ("updatedat", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ecommerceapp.category",
            ),
        ),
    ]
