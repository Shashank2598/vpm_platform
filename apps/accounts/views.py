# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_auth.views import LoginView
from rest_framework import status
from rest_framework.response import Response

from apps.accounts import serializers as accounts_serializers

# Create your views here.

class MembersLoginView(LoginView):

    def get_response(self):
        serializer = accounts_serializers.LoginResponseSerializer(
            instance=self.request.user,
            context={'request': self.request}
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response

