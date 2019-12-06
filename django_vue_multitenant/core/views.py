from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.utils.translation import ugettext as _
from plans.models import Plan
from .mixins import MessageMixin, GetToPostMixin

from django.contrib.auth.views import PasswordChangeView, LoginView

class LandingTemplateView(TemplateView):
    template_name = "landing/index.html"

    def get_context_data(self, **kwargs):
        context = super(LandingTemplateView, self).get_context_data(**kwargs)
        context['plans'] = Plan.objects.all()
        return context


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


class CustomLoginUserView(LoginView):
    
    def dispatch(self, request,*args, **kwargs):
        
        if request.user.is_authenticated:
            group = request.user.groups.filter(user=request.user)
            if group.count():
                if group[0].name=="client":
                    return redirect('clients:clientlandingpage')
            return redirect('products:index')

        return super(CustomLoginUserView, self).dispatch(request, *args, **kwargs)