from django.urls import path, include

from apps.polls.routers import polls_router


urlpatterns = [
    path('auth/', include('apps.users.urls.auth')),
    path('polls/', include(polls_router.urls)),
]
