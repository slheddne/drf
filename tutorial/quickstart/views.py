from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from quickstart.serializers import UserSerializer, GroupSerializer


# ViewSet -> User viewset to represent the User model
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)  # Only authenticated users can view or edit the users


# ViewSet -> Group viewset to represent the Group model
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)  # Only authenticated users can view or edit the groups
