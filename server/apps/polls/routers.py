from rest_framework import routers

from .viewsets import SurveyViewSet


polls_router = routers.DefaultRouter()

polls_router.register(
    prefix='surveys',
    viewset=SurveyViewSet,
    basename='surveys',
)
