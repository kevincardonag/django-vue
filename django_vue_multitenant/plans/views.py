from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.utils.translation import ugettext as _

from core.mixins import MessageMixin
from plans.forms import PlanForm
from plans.models import Plan
from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import TemplateDataMixin


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
            "url_opcion": "plans:detail",
            "parametros_url": ["id"],
            "icono": 'fa-eyes',
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
    delete_message = "Plan eliminado con exito"

    def get_success_url(self):
        return reverse('plans:index')


class PlanDetailView(LoginRequiredMixin, DetailView):
    model = Plan
    template_name = 'plans/detail.html'