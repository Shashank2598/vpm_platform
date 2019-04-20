from rest_framework import serializers

from apps.accounts import models as accounts_models


class LoginResponseSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source='auth_token')

    class Meta:
        model = accounts_models.BaseUser
        fields = ('key', 'first_name', 'last_name', 'email')