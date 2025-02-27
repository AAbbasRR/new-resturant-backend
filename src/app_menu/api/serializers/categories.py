from rest_framework import serializers

from app_menu.models import CategoryModel, FoodModel, FoodItemModel


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItemModel
        fields = ("id", "name", "price")


class FoodSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField("get_items")

    class Meta:
        model = FoodModel
        fields = ("id", "name", "material", "image", "price", "items")

    def __init__(self, *args, **kwargs):
        super(FoodSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")

    def get_items(self, obj):
        return FoodItemSerializer(obj.food_items.all(), many=True, read_only=True).data


class ListCategoriesSerializer(serializers.ModelSerializer):
    category_foods = serializers.SerializerMethodField("get_category_foods")

    class Meta:
        model = CategoryModel
        fields = (
            "id",
            "name",
            "icon",
            "description",
            "category_foods",
        )

    def __init__(self, *args, **kwargs):
        super(ListCategoriesSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")

    def get_category_foods(self, obj):
        return FoodSerializer(
            obj.category_foods.filter(is_active=True).order_by("location"),
            many=True,
            read_only=True,
            context=self.context,
        ).data
