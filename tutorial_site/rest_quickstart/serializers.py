from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest_quickstart.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = [
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]
