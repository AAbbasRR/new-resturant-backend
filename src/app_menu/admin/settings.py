from django.contrib import admin

from app_menu.models import SettingsModel, BranchesModel, BranchCallNumbersModel


class BranchCallNumbersAdmin(admin.TabularInline):
    model = BranchCallNumbersModel
    extra = 0
    min_num = 0


class BranchesAdmin(admin.ModelAdmin):
    inlines = [BranchCallNumbersAdmin]
    list_display = (
        "title",
        "address",
    )
    search_fields = ("title",)

    class Meta:
        model = BranchesModel


class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "favicon",
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


admin.site.register(BranchesModel, BranchesAdmin)
admin.site.register(SettingsModel, SettingsAdmin)
