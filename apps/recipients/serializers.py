from rest_framework import serializers

from apps.recipients import models as recipients_models


class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = recipients_models.Recipient
        fields = (
            'name', 'gender', 'institute_name',
            'standard', 'financial_assistance',
            'description', 'profile_pic'
        )


class SocialAcitivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = recipients_models.SocialActivity
        fields = ('title', 'description', 'financial_assistance', 'image')
