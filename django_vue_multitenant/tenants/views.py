import datetime
import random
import string

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse

from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import TemplateDataMixin, MessageMixin
from core.views import SwitchActiveView
from django_tenants.utils import tenant_context

from users.models import UserProfile
from tenants.models import Pizzeria, PizzeriaRequest, Domain
from tenants.forms import PizzeriaRequestForm, PizzeriaForm
from plans.models import Plan


class PizzeriaCreateView(MessageMixin, CreateView):
    model = Pizzeria
    form_class = PizzeriaForm
    template_name = 'franchises/franchise/create.html'

    def get_context_data(self, **kwargs):
        context = super(PizzeriaCreateView, self).get_context_data(**kwargs)
        context['request_object'] = get_object_or_404(PizzeriaRequest, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        instance = form.instance
        request = get_object_or_404(PizzeriaRequest, pk=self.kwargs['pk'])
        instance.request = request
        instance.schema_name = instance.name.lower().replace(" ", '_')
        instance.paid_until = datetime.datetime.now() + datetime.timedelta(days=30)
        instance.phones = request.phone
        instance.email = request.email
        instance.address = request.address
        instance.plan = request.plan
        instance = form.save()
        domain = Domain()
        domain.domain = form.cleaned_data['domain'].lower().replace(" ", "_") + ".localhost"
        domain.is_primary = True
        domain.tenant = instance
        domain.save()
        with tenant_context(instance):
            password = "".join([random.choice(string.ascii_lowercase[:26]) for i in range(8)])
            # password = 'admin1234'
            user = UserProfile.objects.create(
                first_name='admin',
                last_name="admin",
                email=request.email,
            )
            groups = {
                'admin': [],
                'vendedor': [],
                'client': [],
            }
            for key, value in groups.items():
                created, group = Group.objects.get_or_create(name=key)
            group = Group.objects.get(name="admin")
            user.is_staff = True
            user.set_password(password)
            user.is_superuser = True
            user.save()
            user.groups.add(group)

        send_mail(subject="Bienvenido a superdroguerias",
                  message="Su solicitud de franquicia ha sido creado con exito. utilice el usario 'admin' y"
                          " la contraseña " + password + " para loguearse.",
                  from_email="administracion@superdroguerias.com", recipient_list=[request.email])

        request.is_active = False
        request.save()
        return super(PizzeriaCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('tenants:index')


class PizzeriaSwitchActiveView(PermissionRequiredMixin, SwitchActiveView):

    model = Pizzeria
    success_message = _("El estado de la notaría ha sido actualizado correctamente")
    redirect_url = 'tenants:list'
    raise_exception = True


class PizzeriaListView(TemplateDataMixin, DatatablesListView):
    model = Pizzeria
    raise_exception = True
    page_title = _("Listar Pizzerias")
    section_title = _("Listar Pizzerias")
    model_name = _("Pizzería")
    fields = ["is_active", "name", "address", "phones", "email", ]
    column_names_and_defs = [_("Estado"), _("Nombre"), _("Dirección"), _("Telefonos"), _("Email")]
    options_list = [
        {
            "label_opcion": _('Eiminar'),
            "url_opcion": "tenants:delete_pizzeria",
            "parametros_url": ["id"],
            "icono": 'fa-trash',
            "object_modal_delete": 'dd',
        },
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
    fields = ["representative_full_name", "company_name", "email", "phone",  "address"]
    column_names_and_defs = [_("Nombre representante"), _("company_name"), _("Correo"), _("Teléfono"), _("Dirección"),]
    options_list = [
        {
            "label_opcion": _('Consultar'),
            "url_opcion": "tenants:detail_request_tenant",
            "parametros_url": ["id"],
            "icono": 'fa-eye',
            "confirm_modal": 'ajax-base-modal',
        },
        {
            "label_opcion": _('Eliminar'),
            "url_opcion": "tenants:delete_request_tenant",
            "parametros_url": ["id"],
            "icono": 'fa-trash',
            "object_modal_delete": 'dd',
        }
    ]

    def dispatch(self, request, *args, **kwargs):
        self.queryset = PizzeriaRequest.objects.filter(is_active=True)
        return super(RequestPizzeriaListView, self).dispatch(request, *args, **kwargs)


class RequestPizzeriaDeleteView(LoginRequiredMixin, MessageMixin, DeleteView):
    """
        Autor: Caros Almario
        Fecha: Septiembre 29 2019
        Vista para borrar las solicitudes de pizzeria
    """
    model = PizzeriaRequest

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            try:
                request_pizzeria = get_object_or_404(PizzeriaRequest, pk=kwargs['pk'])
                request_pizzeria.delete()
                return JsonResponse({'status': 1, 'message': 'La solicitud fue eliminada con éxito', 'type': 'success'})
            except Exception:
                return JsonResponse({'status': 0, 'message': 'Ha ocurrido un error', 'type': 'error'})


class RequestPizzeriaDetailView(LoginRequiredMixin, DetailView):
    model = PizzeriaRequest
    template_name = 'requestpizzeria/detail.html'

    def get_context_data(self, **kwargs):
        context = super(RequestPizzeriaDetailView, self).get_context_data(**kwargs)
        context['form'] = PizzeriaForm
        return context


class PizzeriaDeleteView(LoginRequiredMixin, MessageMixin, DeleteView):
    model = Pizzeria

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            try:
                plan = get_object_or_404(Pizzeria, pk=kwargs['pk'])
                plan.delete()
                return JsonResponse({'status': 1, 'message': 'El plan fue eliminado con éxito', 'type': 'success'})
            except Exception:
                return JsonResponse({'status': 0, 'message': 'Ha ocurrido un error', 'type': 'error'})

