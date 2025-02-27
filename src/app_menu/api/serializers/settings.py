from rest_framework import serializers

from app_menu.models import SettingsModel


class MenuInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = (
            "id",
            "title",
            "address",
            "favicon",
            "call_number",
            "instagram_id",
            "open_time",
            "close_time",
            "banner",
        )

    def __init__(self, *args, **kwargs):
        super(MenuInfoSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")
