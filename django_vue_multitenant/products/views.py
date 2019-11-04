
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.utils.translation import ugettext as _

from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import MessageMixin, TemplateDataMixin
from plans.forms import PlanForm
from plans.models import Plan
from django.http.response import JsonResponse

from products.forms import IngredientForm
from products.models import Ingredient


class IngredientListView(LoginRequiredMixin, TemplateDataMixin, DatatablesListView):
    model = Ingredient
    page_title = _("Ingredientes")
    section_title = _("Listado de ingredientes")
    model_name = _("Ingrediente")
    fields = ["name",  "price"]
    create_reversible_url = 'products:create_ingredients'
    column_names_and_defs = [_("Nombre"), _("Precio")]
    options_list = [
        {
            "label_opcion": _('Editar'),
            "url_opcion": 'products:update_ingredients',
            "parametros_url": ["id"],
            "icono": 'fa-pencil-alt',
            "confirm_modal": 'ajax-base-modal',
        },
        {
            "label_opcion": _('Eiminar'),
            "url_opcion": "products:delete_ingredients",
            "parametros_url": ["id"],
            "icono": 'fa-trash',
            "object_modal_delete": 'dd',
        }
    ]


class IngredientCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/create.html"
    success_message = "Ingrediente creado exitosamente"

    def get_success_url(self):
        return reverse('products:list_ingredients')


class IngredientUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/update.html"
    success_message = "Ingrediente modificado exitosamente"

    def get_success_url(self):
        return reverse('products:list_ingredients')


class IngredientDeleteView(LoginRequiredMixin, MessageMixin, DeleteView):

    model = Ingredient

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            try:
                plan = get_object_or_404(Plan, pk=kwargs['pk'])
                plan.delete()
                return JsonResponse({'status': 1, 'message': 'El Ingrediente fue eliminado con éxito', 'type': 'success'})
            except Exception:
                return JsonResponse({'status': 0, 'message': 'Ha ocurrido un error', 'type': 'error'})


class IngredientDetailView(LoginRequiredMixin, DetailView):
    model = Ingredient
    template_name = 'ingredients/detail.html'

