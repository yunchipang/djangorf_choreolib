from rest_framework import serializers
from choreos.models import Choreography, Choreographer, STYLE_CHOICES, PRONOUNS_CHOICES


class ChoreographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Choreography
        fields = ['id', 'created', 'choreographer', 'music_title', 'style', 'video_url']


class ChoreographerSerializer(serializers.Serializer):
    class Meta:
        model = Choreographer
        fields = ['id', 'name', 'pronouns', 'based_in', 'intro', 'instagram_handle']