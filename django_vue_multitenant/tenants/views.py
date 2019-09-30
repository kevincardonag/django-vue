from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic import CreateView
from django.urls import reverse

from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import TemplateDataMixin, MessageMixin
from core.views import SwitchActiveView
from tenants.models import Pizzeria, PizzeriaRequest
from tenants.forms import PizzeriaRequestForm
from plans.models import Plan


class PizzeriaSwitchActiveView(PermissionRequiredMixin, SwitchActiveView):
    """
    Autor: Milton Lenis
    Fecha: Marzo 28 2017
    Vista para cambiar el estado entre activo e inactivo de una notaría
    """
    model = Pizzeria
    success_message = _("El estado de la notaría ha sido actualizado correctamente")
    redirect_url = 'tenants:list'
    #permission_required = 'tenants.change_notaria'
    raise_exception = True


class PizzeriaListView(TemplateDataMixin, DatatablesListView):
    """
    Autor: Milton Lenis
    Fecha: Marzo 27 2017
    Vista para listar notarías
    """
    model = Pizzeria
    #permission_required = 'tenants.list_notaria'
    raise_exception = True
    page_title = _("Listar Pizzerias")
    section_title = _("Listar Pizzerias")
    model_name = _("Notaría")
    #create_reversible_url = 'tenants:create'
    fields = ["is_active", "name", "address", "phones", "email", "has_physical_delivers"]
    column_names_and_defs = [_("Estado"), _("Nombre"), _("Dirección"), _("Telefonos"), _("Email"),
                             _("Acepta envios"),]
    options_list = [

    ]

    def dispatch(self, request, *args, **kwargs):
        self.queryset = self.model.objects.exclude(id=request.tenant.id)
        return super(PizzeriaListView, self).dispatch(request, *args, **kwargs)

    def get_rendered_html_value(self, field, value):  # pragma: no cover
        self.html_value = super(PizzeriaListView, self).get_rendered_html_value(field, value)

        if field.name == 'is_active':
            if value:
                self.html_value = '<label class="label label-success">{0}</label>'.format(_('ACTIVO'))
            else:
                self.html_value = '<label class="label label-danger">{0}</label>'.format(_('INACTIVO'))
        elif field.name == 'has_physical_delivers':
            if value:
                self.html_value = '<span class="display-block text-center">{0}</span>'.format(_('SÍ'))
            else:
                self.html_value = '<span class="display-block text-center">{0}</span>'.format(_('NO'))
        return self.html_value


class RequestPizzeriaCreateView(MessageMixin, CreateView):
    """
        Autor: Caros Almario
        Fecha: Septiembre 29 2019
        Vista para crear las solicitudes de las franquicias
    """
    model = PizzeriaRequest
    form_class = PizzeriaRequestForm
    template_name = 'requestpizzeria/create.html'
    success_message = "Tu solicitud ha sido enviada con exito."

    def get_context_data(self, **kwargs):
        context = super(RequestPizzeriaCreateView, self).get_context_data(**kwargs)
        context['plan'] = get_object_or_404(Plan, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        instance = form.instance
        plan = get_object_or_404(Plan, pk=self.kwargs['pk'])
        instance.plan = plan
        form.save()
        return super(RequestPizzeriaCreateView, self).form_valid(form)

    def get_success_url(self):
            return reverse('index')


class RequestPizzeriaListView(TemplateDataMixin, DatatablesListView):
    """
        Autor: Caros Almario
        Fecha: Septiembre 29 2019
        Vista para lisar las solicutdes de las franquicias
    """
    model = PizzeriaRequest
    page_title = _("Solicitudes")
    section_title = _("Solicitudes de franquicias")
    model_name = _("Solicitud")
    fields = ["name", "last_name", "email", "phone"]
    column_names_and_defs = [_("Nombre"), _("Apellido"), _("Correo"), _("Teléfono"), ]
    options_list = [

    ]