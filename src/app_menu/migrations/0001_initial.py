# Generated by Django 4.1.7 on 2023-06-15 06:25

import app_menu.models.category
import app_menu.models.food
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "icon",
                    models.ImageField(
                        upload_to=app_menu.models.category.category_icon_directory_path,
                        verbose_name="Icon",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Food",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("material", models.TextField(verbose_name="Material")),
                (
                    "image",
                    models.ImageField(
                        upload_to=app_menu.models.food.food_image_directory_path,
                        verbose_name="تصویر",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "price",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Price",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="category_foods",
                        to="app_menu.category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Food",
                "verbose_name_plural": "Foods",
            },
        ),
    ]
