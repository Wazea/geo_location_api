from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view

from geo_location_api.serializers import UserSerializer, GroupSerializer
from geo_location_api.services import CoordinatesPlotter


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated],


@api_view()
def init_plotter(self):
    coordinates_plotter = CoordinatesPlotter()
    try:
        coordinates_plotter.plot_coordinates_on_map()
    except RuntimeError:
        return JsonResponse({"success": False}, status=503)

    return JsonResponse({"success": True})
