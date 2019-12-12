import datetime
import json
import os
import random
import shutil
import string

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse, FileResponse
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse

from api_rest.serializers import OrderJsonSerializer, ProductJsonSerializer, IngredientJsonSerializer, \
    UserJsonSerializer, TenantJsonSerializer
from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import TemplateDataMixin, MessageMixin
from core.views import SwitchActiveView
from django_tenants.utils import tenant_context

from products.models import Product, Ingredient
from users.models import UserProfile
from tenants.models import Pizzeria, PizzeriaRequest, Domain
from tenants.forms import PizzeriaRequestForm, PizzeriaForm
from plans.models import Plan
from django.core.mail import EmailMessage

from orders.models import Order


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
        instance.date_expired_paid = datetime.date.today() + datetime.timedelta(days=30)
        instance.phones = request.phone
        instance.email = request.email
        instance.address = request.address
        instance.plan = request.plan
        instance = form.save()
        domain = Domain()
        domain.domain = form.cleaned_data['domain'].lower().replace(" ", "_") + "."+self.request.tenant.domains.first().domain
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

        send_mail(
            subject="Bienvenido a SuperPizzas",
            message="Su solicitud de franquicia ha sido creado con exito. utilice el correo "+request.email+" y"
                      " la contraseña " + password + " para loguearse. url: "+domain.domain,
            from_email="administracion@superpizzas.com",
            recipient_list=[request.email])

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


class PizzeriaListView(LoginRequiredMixin, TemplateDataMixin, DatatablesListView):
    model = Pizzeria
    raise_exception = True
    page_title = _("Listar Pizzerias")
    section_title = _("Listar Pizzerias")
    model_name = _("Pizzería")
    fields = ["is_active", "name", "address", "phones", "email", "requested_to_retire"]
    column_names_and_defs = [_("Estado"), _("Nombre"), _("Dirección"), _("Telefonos"), _("Email"), _("Solicitud de retiro")]
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
        elif field.name == 'requested_to_retire':
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
        cc_number = instance.cc_number
        init_cc = cc_number[:-4]
        cc = list(map(lambda n: "*", init_cc))
        full_cc_number = "".join(cc) + cc_number[-4:]
        instance.cc_number = full_cc_number
        form.save()
        return super(RequestPizzeriaCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return redirect(reverse("index"))

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


class RequestRetirePizzeriaView(LoginRequiredMixin, MessageMixin, View):
    model = Pizzeria

    def get(self, request, *args, **kwargs):
        try:
            pizzeria = get_object_or_404(Pizzeria, pk=kwargs['pk'])
            pizzeria.requested_to_retire = True
            pizzeria.save()

            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Crear carpeta al usuario
            user_path = os.path.join(settings.BASE_DIR, '..', "user_request_data/", str(request.user.id) + date)
            user_relative_path = self.create_folder(user_path)
            print("Se crea la carpeta global para el usuario.")

            orders = Order.objects.all()
            self.serializer_model(orders, user_relative_path, "ordenes", OrderJsonSerializer)

            products = Product.objects.all()
            self.serializer_model(products, user_relative_path, "productos", ProductJsonSerializer)

            ingredients = Ingredient.objects.all()
            self.serializer_model(ingredients, user_relative_path, "ingredientes", IngredientJsonSerializer)

            tenants = [request.tenant]
            self.serializer_model(tenants, user_relative_path, "pizzeria", TenantJsonSerializer)

            users = UserProfile.objects.all()
            self.serializer_model(users, user_relative_path, "usuarios", UserJsonSerializer)

            location_zip = os.path.join(settings.BASE_DIR, '..', "user_request_data/", str(request.user.id))
            shutil.make_archive(location_zip + "/", 'zip', user_relative_path)
            print("Los datos del usuario se comprimieron con éxito en formato .zip")
            messages.success(self.request, "Su solicitud ha sido recibida con éxito")
            return FileResponse(open(location_zip + ".zip", 'rb'))

        except Exception as error:
            print(error)
            messages.error(self.request, "Ocurrio un error,intente de nuevo.")
            return redirect(request.META['HTTP_REFERER'])

    def serializer_model(self, _objects, user_relative_path, name_model, model_serializer):
        data = []
        with open(user_relative_path + f"/{name_model}.json", "w+") as file:
            for _object in _objects:
                serializer = model_serializer(_object)
                data.append(serializer.data)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def create_folder(self, path, obj=None):
        if obj:
            relative_path = path + "/" + str(obj.id)
        else:
            relative_path = path

        try:
            os.mkdir(relative_path)
            return relative_path
        except OSError as error:
            print(error)
            print("Se ha producido un error al tratar de crear la carpeta")