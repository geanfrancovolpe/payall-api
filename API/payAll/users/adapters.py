# -*- coding: utf-8 -*-

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomAllauthAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        super().send_mail(template_prefix, email, context)