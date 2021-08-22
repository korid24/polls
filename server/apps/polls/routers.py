from rest_framework import routers

from .viewsets import AnswerViewSet, AnswerChoiceViewSet, QuestionViewSet, SurveyViewSet


polls_router = routers.DefaultRouter()

polls_router.register(
    prefix='surveys',
    viewset=SurveyViewSet,
    basename='surveys',
)
polls_router.register(
    prefix='questions',
    viewset=QuestionViewSet,
    basename='questions',
)
polls_router.register(
    prefix='answer-choices',
    viewset=AnswerChoiceViewSet,
    basename='answer_choices',
)
polls_router.register(
    prefix='answers',
    viewset=AnswerViewSet,
    basename='answers',
)
