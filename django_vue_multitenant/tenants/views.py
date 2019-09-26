from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.utils.translation import ugettext as _


from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import TemplateDataMixin
from core.views import SwitchActiveView
from tenants.models import Pizzeria


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
