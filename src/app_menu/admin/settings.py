from django.contrib import admin

from app_menu.models import SettingsModel


class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "address",
        "favicon",
        "call_number",
        "instagram_id",
        "open_time",
        "close_time",
        "banner",
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return not SettingsModel.objects.exists()

    class Meta:
        model = SettingsModel


admin.site.register(SettingsModel, SettingsAdmin)
