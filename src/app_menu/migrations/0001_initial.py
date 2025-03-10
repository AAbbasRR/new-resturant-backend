# Generated by Django 4.2.2 on 2025-02-27 09:24

import app_menu.models.category
import app_menu.models.food
import app_menu.models.settings
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
                ("name", models.CharField(max_length=100, verbose_name="نام")),
                (
                    "icon",
                    models.ImageField(
                        upload_to=app_menu.models.category.category_icon_directory_path,
                        verbose_name="آیکون",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="وضعیت فعال بودن"),
                ),
                (
                    "location",
                    models.PositiveIntegerField(default=1, verbose_name="جایگاه"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="توضیحات"),
                ),
            ],
            options={
                "verbose_name": "دسته",
                "verbose_name_plural": "دسته ها",
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
                ("name", models.CharField(max_length=100, verbose_name="نام")),
                (
                    "material",
                    models.TextField(blank=True, null=True, verbose_name="رسپی"),
                ),
                (
                    "image",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=app_menu.models.food.food_image_directory_path,
                        verbose_name="عکس",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="وضعیت فعال بودن"),
                ),
                (
                    "price",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="قیمت",
                    ),
                ),
                (
                    "location",
                    models.PositiveIntegerField(default=1, verbose_name="جایگاه"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="category_foods",
                        to="app_menu.category",
                        verbose_name="دسته",
                    ),
                ),
            ],
            options={
                "verbose_name": "غذا",
                "verbose_name_plural": "غذاها",
            },
        ),
        migrations.CreateModel(
            name="Settings",
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
                ("title", models.CharField(max_length=100, verbose_name="عنوان")),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="آدرس"
                    ),
                ),
                (
                    "favicon",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=app_menu.models.settings.setting_image_directory_path,
                        verbose_name="آیکون",
                    ),
                ),
                (
                    "call_number",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="شماره تماس"
                    ),
                ),
                (
                    "open_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="زمان شروع کار"
                    ),
                ),
                (
                    "close_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="زمان پایان کار"
                    ),
                ),
                (
                    "banner",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=app_menu.models.settings.setting_image_directory_path,
                        verbose_name="بنر",
                    ),
                ),
            ],
            options={
                "verbose_name": "تنظیمات رستوران",
                "verbose_name_plural": "تنظیمات رستوران",
            },
        ),
        migrations.CreateModel(
            name="FoodItem",
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
                ("name", models.CharField(max_length=100, verbose_name="نام")),
                (
                    "price",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="قیمت",
                    ),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="food_items",
                        to="app_menu.food",
                        verbose_name="غذا",
                    ),
                ),
            ],
            options={
                "verbose_name": "آیتم(سایز، نوع متفاوت)",
                "verbose_name_plural": "آیتم ها(سایز، نوع متفاوت)",
            },
        ),
    ]
