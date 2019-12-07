import datetime

from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.urls import reverse


class VerifyActivePlan:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.tenant == "public":
            current_date = datetime.date.today()
            if request.tenant.date_expired_paid:
                if current_date > request.tenant.date_expired_paid:
                    if not request.path == reverse('plans:upgrade_plan'):
                        return redirect(reverse('plans:upgrade_plan'))


        # Code to be executed for each request/response after
        # the view is called.

        return response