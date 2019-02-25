"""
Middleware Class for redirecting user based on there type (Main, Admin, Manager, StoreKeeper)
"""

import re

from django.http import HttpResponsePermanentRedirect
from project.core.apps.user_api.models import UserType


class UserTypeBaseRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    @staticmethod
    def process_request(request):

        if request.user.is_authenticated:
            host = request.META['HTTP_HOST'] + request.META['PATH_INFO']
            user_type = UserType.objects.get(user=request.user)

            main_user_site = r'$/main/$'
            admin_user_site = r'$/admins/$'
            manager_user_site = r'$/manager/$'
            store_keeper_user_site = r'$/store-keeper/$'
            if request.user.is_superuser and re.compile(r'/admin/$').match(host) is False:
                return HttpResponsePermanentRedirect('/')
            if user_type.is_main_user and re.compile(main_user_site).match(host) is False:
                print(user_type.is_main_user)
                return HttpResponsePermanentRedirect('/main/')
            if user_type.is_admin_user and re.compile(admin_user_site).match(host) is False:
                return HttpResponsePermanentRedirect('/admins/')
            if user_type.is_admin_user and re.compile(manager_user_site).match(host) is False:
                return HttpResponsePermanentRedirect('/manager/')
            if user_type.is_admin_user and re.compile(store_keeper_user_site).match(host) is False:
                return HttpResponsePermanentRedirect('/store-keeper/')
            return None
        return None


