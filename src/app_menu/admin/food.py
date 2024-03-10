from django.contrib import admin

from app_menu.models import FoodModel, FoodItemModel


class FoodItemAdmin(admin.TabularInline):
    model = FoodItemModel
    extra = 0
    min_num = 0


class FoodsAdmin(admin.ModelAdmin):
    inlines = [FoodItemAdmin]
    list_display = (
        "name",
        "category",
        "location",
        "material",
        "is_active",
        "price",
    )
    search_fields = (
        "name",
        "material",
    )

    class Meta:
        model = FoodModel


admin.site.register(FoodModel, FoodsAdmin)
