from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers import RoleBasedTokenObtainPairSerializer


class RoleBasedTokenObtainPairView(TokenObtainPairView):
    serializer_class = RoleBasedTokenObtainPairSerializer
