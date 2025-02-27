from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator

from config.settings import DEBUG

from app_menu.models import CategoryModel


def food_image_directory_path(instance, filename):
    return "food_images/{0}".format(filename)


class Food(models.Model):
    class Meta:
        verbose_name = _("Food")
        verbose_name_plural = _("Foods")

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.SET_NULL,
        related_name="category_foods",
        null=True,
        verbose_name=_("Category"),
    )
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    material = models.TextField(null=True, blank=True, verbose_name=_("Material"))
    image = models.FileField(
        upload_to=food_image_directory_path,
        null=True,
        blank=True,
        verbose_name=_("Image"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    price = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], verbose_name=_("Price")
    )
    location = models.PositiveIntegerField(default=1, verbose_name=_("Location"))

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.pk is None:
            onother_location = Food.objects.filter(
                category=self.category, location=self.location
            ).first()
            if onother_location is not None:
                last_obj = (
                    Food.objects.filter(category=self.category)
                    .order_by("location")
                    .last()
                )
                self.location = last_obj.location + 1
        return super().save(force_insert, force_update, using, update_fields)


class FoodItem(models.Model):
    class Meta:
        verbose_name = _("Food Item")
        verbose_name_plural = _("Food Items")

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name="food_items",
        verbose_name=_("Food"),
    )
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    price = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], verbose_name=_("Price")
    )
