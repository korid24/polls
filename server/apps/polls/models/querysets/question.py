from django.db.models import QuerySet, Case, When, Q, Value, BooleanField
from django.utils import timezone


class QuestionQuerySet(QuerySet):
    def annotate_with_is_active(self) -> 'QuestionQuerySet':
        today = timezone.now().date()

        return self.annotate(
            is_active=Case(
                When(
                    Q(survey__start_date__lte=today) & Q(survey__end_date__gte=today),
                    then=Value(True),
                ),
                default=Value(False),
                output_field=BooleanField(),
            ),
        )
