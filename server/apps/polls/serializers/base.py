from rest_framework import serializers

from ..models import Survey


class SurveyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name')
