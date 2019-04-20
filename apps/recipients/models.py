# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Recipient(models.Model):

    MALE = True
    FEMALE = False

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    name = models.CharField(max_length=30)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(200)])
    institute_name = models.CharField(max_length=255)
    standard = models.CharField(max_length=128)
    financial_assistance = models.PositiveIntegerField()
    description = models.CharField(max_length=10000)
    profile_pic = models.ImageField(
        upload_to='images/profile_pictures/',
        blank=True,
        default='images/profile_pictures/default.jpg'
    )

    def __unicode__(self):
        return self.name


class SocialActivity(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    financial_assistance = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='images/social_activities/',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.title