from datetime import date
from typing import Final, Any

from rest_framework import serializers

from ..models import Survey


class SurveyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name')


class SurveyUpdateSerializer(SurveyBaseSerializer):
    class Errors:
        WRONG_END_DATE: Final[str] = 'Дата окончания не может быть раньше даты начала'

    class Meta(SurveyBaseSerializer.Meta):
        fields = SurveyBaseSerializer.Meta.fields + ('end_date', 'description')

    def validate_end_date(self, end_date: date) -> date:
        if self.instance and end_date < self.instance.start_date:
            raise serializers.ValidationError(self.Errors.WRONG_END_DATE)

        return end_date


class SurveySerializer(SurveyUpdateSerializer):
    class Meta(SurveyUpdateSerializer.Meta):
        fields = SurveyUpdateSerializer.Meta.fields + ('start_date',)

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        if attrs['end_date'] < attrs['start_date']:
            raise serializers.ValidationError({'end_date': self.Errors.WRONG_END_DATE})

        return attrs
