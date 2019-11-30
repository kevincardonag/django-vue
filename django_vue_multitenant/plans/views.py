import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.utils.translation import ugettext as _

from core.mixins import MessageMixin
from plans.forms import PlanForm, PaymentForm
from plans.models import Plan
from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import TemplateDataMixin
from django.http.response import JsonResponse

from tenants.models import Pizzeria


class PlanListView(LoginRequiredMixin, TemplateDataMixin, DatatablesListView):
    """
        Autor: Caros Almario
        Fecha: Septiembre 29 2019
        Vista para listar los planes
    """
    model = Plan
    page_title = _("Planes")
    section_title = _("Listado de Planes")
    model_name = _("Plan")
    fields = ["name", "description", "price"]
    create_reversible_url = 'plans:create'
    column_names_and_defs = [_("Nombre"), _("Descripción"), _("Precio")]
    options_list = [
        {
            "label_opcion": _('Editar'),
            "url_opcion": "plans:update",
            "parametros_url": ["id"],
            "icono": 'fa-pencil-alt',
            "confirm_modal": 'ajax-base-modal',
        },
        {
            "label_opcion": _('Eiminar'),
            "url_opcion": "plans:delete",
            "parametros_url": ["id"],
            "icono": 'fa-trash',
            "object_modal_delete": 'dd',
        }
    ]


class PlanCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    """
        Autor: Caros Almario
        Fecha: Septiembre 29 2019
        Vista para crear los planes
    """
    model = Plan
    form_class = PlanForm
    template_name = 'plans/create.html'
    success_message = "Plan creado exitosamente"

    def get_success_url(self):
        return reverse('plans:index')


class PlanUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    """
        Autor: Caros Almario
        Fecha: Septiembre 29 2019
        Vista para actualizar los planes
    """
    model = Plan
    form_class = PlanForm
    template_name = 'plans/update.html'
    success_message = "Plan modificado exitosamente"

    def get_success_url(self):
        return reverse('plans:index')


class PlanDeleteView(LoginRequiredMixin, MessageMixin, DeleteView):
    """
        Autor: Caros Almario
        Fecha: Septiembre 29 2019
        Vista para borrar los planes
    """
    model = Plan

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            try:
                plan = get_object_or_404(Plan, pk=kwargs['pk'])
                plan.delete()
                return JsonResponse({'status': 1, 'message': 'El plan fue eliminado con éxito', 'type': 'success'})
            except Exception:
                return JsonResponse({'status': 0, 'message': 'Ha ocurrido un error', 'type': 'error'})


class PlanDetailView(LoginRequiredMixin, DetailView):
    model = Plan
    template_name = 'plans/detail.html'


class PlanUpgradeListView(LoginRequiredMixin, TemplateDataMixin, ListView):
    model = Plan
    template_name = 'plans/upgrade_user_plan.html'
    page_title = _("Planes")
    section_title = _("Listado de Planes")
    model_name = _("Plan")

    def get_context_data(self, **kwargs):
        context = super(PlanUpgradeListView, self).get_context_data()
        context['payment_form'] = PaymentForm()
        return context


class PlanUpgradeUpdateView(LoginRequiredMixin, TemplateDataMixin, UpdateView):
    model = Plan
    form_class = PaymentForm
    template_name = 'plans/upgrade_user_plan.html'
    page_title = _("Planes")
    section_title = _("Listado de Planes")
    model_name = _("Plan")

    def post(self, request, *args, **kwargs):
        full_name = self.request.POST.get("full_name")
        identification = self.request.POST.get("identification")
        cc_number = self.request.POST.get("cc_number")
        cc_expiry = self.request.POST.get("cc_expiry")
        cc_code = self.request.POST.get("cc_code")
        tenant = self.request.tenant
        tenant.cc_number = cc_number
        tenant.cc_expiry = cc_expiry
        tenant.cc_code = cc_code
        current_day = datetime.date.today()
        date_next_payment = current_day + datetime.timedelta(days=30)
        tenant.date_expired_paid = date_next_payment
        #import pdb;pdb.set_trace()
        tenant.plan = self.get_object()
        tenant.save()

        return redirect(reverse("plans:upgrade_plan"))
