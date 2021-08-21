from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..constants import Roles


class RoleBasedTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: dict) -> dict:
        data = super().validate(attrs)
        data['role'] = Roles.ADMIN if self.user.is_superuser else Roles.USER
        return data
