from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from ..views import RoleBasedTokenObtainPairView


urlpatterns = [
    path(
        route='token/obtain/',
        view=RoleBasedTokenObtainPairView.as_view(),
        name='token_obtain',
    ),
    path(
        route='token/refresh/',
        view=TokenRefreshView.as_view(),
        name='token_refresh',
    ),
]
