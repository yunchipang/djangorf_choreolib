from rest_framework import serializers
from choreos.models import Choreography, STYLE_CHOICES


class ChoreographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Choreography
        fields = ['id', 'created', 'choreographer', 'music_title', 'style', 'video_url']