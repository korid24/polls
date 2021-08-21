from datetime import date
from typing import Final

from rest_framework import serializers

from ..models import Survey


class SurveyCreateSerializer(serializers.ModelSerializer):
    class Errors:
        WRONG_END_DATE: Final[str] = 'Дата окончания не может быть раньше даты начала'

    class Meta:
        model = Survey
        fields = ('id', 'start_date', 'end_date', 'description')

    def validate_end_date(self, end_date: date) -> date:
        if end_date < self.data['start_date']:
            raise serializers.ValidationError()

        return end_date
