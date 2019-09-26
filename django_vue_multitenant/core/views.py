from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.utils.translation import ugettext as _

from .mixins import MessageMixin, GetToPostMixin


class LandingTemplateView(TemplateView):
    template_name = "landing/index.html"


class SwitchActiveView(MessageMixin, SingleObjectMixin, GetToPostMixin, View):
    model = None
    redirect_url = ''
    success_message = _("El estado del registro ha sido actualizado correctamente")

    def get_success_url(self):
        return reverse(self.redirect_url)

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        object.switch_active()
        messages.success(request, self.success_message)
        return redirect(self.get_success_url())
