from rest_framework import serializers

from app_menu.models import CategoryModel, FoodModel, FoodItemModel


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItemModel
        fields = ("id", "name", "price")


class CategorySerializer(serializers.ModelSerializer):
    icon_link = serializers.SerializerMethodField("get_icon_link")

    class Meta:
        model = CategoryModel
        fields = (
            "id",
            "name",
            "description",
            "icon_link",
        )

    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")

    def get_icon_link(self, obj):
        return obj.get_icon_url(self.request)


class ListFoodSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField("get_items")
    category = serializers.SerializerMethodField("get_category")
    image_link = serializers.SerializerMethodField(
        "get_image_link",
    )

    class Meta:
        model = FoodModel
        fields = (
            "id",
            "name",
            "material",
            "price",
            "items",
            "category",
            "image_link",
        )

    def __init__(self, *args, **kwargs):
        super(ListFoodSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")

    def get_items(self, obj):
        return FoodItemSerializer(obj.food_items.all(), many=True, read_only=True).data

    def get_category(self, obj):
        return CategorySerializer(
            obj.category, many=False, read_only=True, context=self.context
        ).data

    def get_image_link(self, obj):
        return obj.get_image_url(self.request)
