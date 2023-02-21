from rest_framework import serializers
from choreos.models import Choreography, STYLE_CHOICES
from django.contrib.auth.models import User


class ChoreographySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Choreography
        fields = ['id', 'created', 'choreographer', 'music_title', 'style', 'video_url', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    choreographies = serializers.PrimaryKeyRelatedField(many=True, queryset=Choreography.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'choreographies']