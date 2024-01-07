from django.contrib.auth.models import User, Group
from rest_framework import serializers

from quickstart.models import Song


# Serializer -> User serializer to represent the User model
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Metaclass to specify the model and fields to be serialized
    class Meta:
        model = User  # Model to be serialized
        fields = ('url', 'username', 'email', 'groups')  # Fields to be serialized


# Serializer -> Group serializer to represent the Group model
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # Metaclass to specify the model and fields to be serialized
    class Meta:
        model = Group  # Model to be serialized
        fields = ('url', 'name')  # Fields to be serialized


# Serializer -> Song serializer to represent the Song model
class SongSerializer(serializers.HyperlinkedModelSerializer):
    # Metaclass to specify the model and fields to be serialized
    class Meta:
        model = Song  # Model to be serialized
        fields = ('title', 'release_year')  # Fields to be serialized
