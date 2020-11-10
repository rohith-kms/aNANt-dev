#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:17:59 2020

@author: ashish
"""

from django.contrib.auth.tokens import PasswordResetTokenGenerator  
from django.utils import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):  
        def _make_hash_value(self, user, timestamp):  
            return (six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active))
        
        
account_activation_token = AccountActivationTokenGenerator()