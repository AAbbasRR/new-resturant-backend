from rest_framework import serializers

from app_menu.models import SettingsModel, BranchesModel, BranchCallNumbersModel


class BranchCallNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchCallNumbersModel
        fields = ("id", "call_number")


class ListBranchesSerializer(serializers.ModelSerializer):
    call_numbers = serializers.SerializerMethodField("get_call_numbers")

    class Meta:
        model = BranchesModel
        fields = (
            "id",
            "title",
            "address",
            "call_numbers",
        )

    def __init__(self, *args, **kwargs):
        super(ListBranchesSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")

    def get_call_numbers(self, obj):
        return BranchCallNumbersSerializer(
            obj.branch_numbers.all(), many=True, read_only=True
        ).data


class MenuInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = (
            "id",
            "title",
            "short_description",
            "favicon",
            "instagram_id",
            "open_time",
            "close_time",
            "banner",
        )

    def __init__(self, *args, **kwargs):
        super(MenuInfoSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")
