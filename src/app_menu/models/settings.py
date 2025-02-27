from django.db import models
from django.utils.translation import gettext as _


class SettingsManager(models.Manager):
    def create_update(self, title, value):
        obj = self.filter(title=title).first()
        if obj is None:
            obj = self.create(title=title, value=value)
        else:
            obj.value = value
            obj.save()
        return obj


def setting_image_directory_path(instance, filename):
    return "setting_images/{0}".format(filename)


class Settings(models.Model):
    class Meta:
        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")

    title = models.CharField(max_length=100, verbose_name=_("Title"))
    address = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Address")
    )
    favicon = models.ImageField(
        null=True,
        blank=True,
        upload_to=setting_image_directory_path,
        verbose_name=_("Favicon"),
    )
    call_number = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=_("Call Number")
    )
    open_time = models.TimeField(null=True, blank=True, verbose_name=_("Open Time"))
    close_time = models.TimeField(null=True, blank=True, verbose_name=_("Close Time"))
    instagram_id = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Instagram ID")
    )
    banner = models.ImageField(
        null=True,
        blank=True,
        upload_to=setting_image_directory_path,
        verbose_name=_("Banner"),
    )

    objects = SettingsManager()
