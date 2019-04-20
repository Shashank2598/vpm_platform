# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from apps.recipients import(
    models as recipients_models,
    serializers as recipients_serializers
)


class RecipientViewset(viewsets.ModelViewSet):
    queryset = recipients_models.Recipient.objects.all()
    serializer_class = recipients_serializers.RecipientSerializer


class SocialActivityViewset(viewsets.ModelViewSet):
    queryset = recipients_models.SocialActivity.objects.all()
    serializer_class = recipients_serializers.SocialActivitySerializer

