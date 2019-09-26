from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.datatables_tools.datatables_tools import DatatablesListView


class TemplateDataMixin(object):

    create_reversible_url = None
    template_name = None

    def get_template_names(self):
        cls = self.__class__
        if self.template_name:
            return self.template_name
        elif issubclass(cls, (DatatablesListView, ListView)):
            return ['_list.html']
        elif issubclass(cls, (UpdateView, CreateView)):
            return ['_form.html']
        elif issubclass(cls, DetailView):
            return ['_detail.html']
        else:
            raise ImproperlyConfigured("{0}: TemplateDataMixin only supports DatatablesListView, ListView, UpdateView, "
                                       "CreateView and DetailView".format(self.__class__.__name__))

    def _get_value(self, attr):
        value = getattr(self, attr, None)
        if value:
            return value
        else:
            raise ImproperlyConfigured("You are using the TemplateDataMixin in {0} but you are not passing "
                                       "'page_title' and 'section_title' attributes".format(self.__class__.__name__))

    def _get_model_name(self):

        model_name = getattr(self, 'model_name', None)
        if not model_name:
            model_name = self.model.__name__
        return model_name.lower()

    def _get_and_reverse_create_url(self):
        return reverse(self.create_reversible_url)

    def get_context_data(self, **kwargs):
        context = super(TemplateDataMixin, self).get_context_data(**kwargs)
        context.update({
            'page_title': self._get_value('page_title'),
            'section_title': self._get_value('section_title'),
            'model_name': self._get_model_name()
        })
        if self.create_reversible_url:
            context.update({
                'create_url': self._get_and_reverse_create_url()
            })
        return context


class MessageMixin(object):
    # Mensajes por defecto
    success_message = _("La información ha sido actualizada correctamente")
    failure_message = _("El formulario tiene errores, por favor revise la información.")

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.failure_message)
        return super(MessageMixin, self).form_invalid(form)


class GetToPostMixin(object):

    def get(self, request, *args, **kwargs):
        # FIXME: Este método es inseguro, se utiliza solo porque las datatables de rady todavía no soportan este tipo
        # de urls
        if hasattr(super, 'get'):
            super(GetToPostMixin, self).get(request, *args, **kwargs)
        return self.post(request, *args, **kwargs)
