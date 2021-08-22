from django.db.models import Manager

from ..querysets import SurveyQuerySet


class SurveyManager(Manager):
    def get_queryset(self, **kwargs) -> SurveyQuerySet:
        return SurveyQuerySet(
            self.model,
            using=self._db,
        )

    def annotate_with_is_active(self) -> SurveyQuerySet:
        return self.get_queryset().annotate_with_is_active()

    def annotate_with_is_passed(self, user_id: int) -> SurveyQuerySet:
        return self.get_queryset().annotate_with_is_passed(user_id=user_id)
