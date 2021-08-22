from django.db.models import Manager

from ..querysets import QuestionQuerySet


class QuestionManager(Manager):
    def get_queryset(self, **kwargs) -> QuestionQuerySet:
        return QuestionQuerySet(
            self.model,
            using=self._db,
        )

    def annotate_with_is_active(self) -> QuestionQuerySet:
        return self.get_queryset().annotate_with_is_active()
