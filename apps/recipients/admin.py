# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from apps.recipients import models as recipients_models


admin.site.register(recipients_models.Recipient)
admin.site.register(recipients_models.SocialActivity)
