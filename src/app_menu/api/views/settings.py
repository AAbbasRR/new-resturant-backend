from rest_framework import generics

from app_menu.api.serializers.settings import MenuInfoSerializer, ListBranchesSerializer
from app_menu.models import SettingsModel, BranchesModel

from utils.versioning import BaseVersioning
from utils.permissions import AllowAnyPermission


class ListBranchesView(generics.ListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    serializer_class = ListBranchesSerializer
    queryset = BranchesModel.objects.all()


class MenuInfoView(generics.ListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    serializer_class = MenuInfoSerializer
    queryset = SettingsModel.objects.all()
