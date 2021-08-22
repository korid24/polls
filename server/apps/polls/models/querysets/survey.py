from django.db.models import QuerySet, Case, When, Q, Value, BooleanField, Exists, OuterRef
from django.utils import timezone


class SurveyQuerySet(QuerySet):
    def annotate_with_is_active(self) -> 'SurveyQuerySet':
        today = timezone.now().date()

        return self.annotate(
            is_active=Case(
                When(
                    Q(start_date__lte=today) & Q(end_date__gte=today),
                    then=Value(True),
                ),
                default=Value(False),
                output_field=BooleanField(),
            ),
        )

    def annotate_with_is_passed(self, user_id: int) -> 'SurveyQuerySet':
        from apps.polls.models import Question

        return self.annotate(
            is_passed=Exists(
                Question.objects.filter(
                    survey_id=OuterRef('pk'),
                    answers__user_id=user_id,
                ),
            ),
        )
