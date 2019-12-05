from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.utils.translation import ugettext as _
from django_tenants.utils import get_tenant_model

from config.settings.base import MAX_PRODUCT_CREATE
from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import MessageMixin, TemplateDataMixin
from plans.models import Plan
from django.http.response import JsonResponse

from products.forms import IngredientForm, ProductForm
from products.models import Ingredient, Product
from tenants.models import Pizzeria


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
                plan = get_object_or_404(Ingredient, pk=kwargs['pk'])
                plan.delete()
                return JsonResponse({'status': 1, 'message': 'El Ingrediente fue eliminado con éxito', 'type': 'success'})
            except Exception:
                return JsonResponse({'status': 0, 'message': 'Ha ocurrido un error', 'type': 'error'})


class IngredientDetailView(LoginRequiredMixin, DetailView):
    model = Ingredient
    template_name = 'ingredients/detail.html'


class ProductListView(LoginRequiredMixin, TemplateDataMixin, DatatablesListView):
    model = Product
    page_title = _("Productos")
    section_title = _("Listado de Productos")
    model_name = _("Producto")
    fields = ["name", "price"]
    create_reversible_url = 'products:create_product'
    class_modal_create = "ajax-modal-large"
    column_names_and_defs = [ _("Nombre"), _("Precio")]
    options_list = [
        {
            "label_opcion": _('Editar'),
            "url_opcion": 'products:update_product',
            "parametros_url": ["id"],
            "icono": 'fa-pencil-alt',
            "confirm_modal": 'ajax-base-modal-large',
            "class_target_modal": 'ajax-modal-large'
        },
        {
            "label_opcion": _('Consultar'),
            "url_opcion": 'products:detail_product',
            "parametros_url": ["id"],
            "icono": 'fa-eye',
            "confirm_modal": 'ajax-base-modal-large',
            "class_target_modal": 'ajax-modal-large'
        },
        {
            "label_opcion": _('Eiminar'),
            "url_opcion": "products:delete_product",
            "parametros_url": ["id"],
            "icono": 'fa-trash',
            "object_modal_delete": 'dd',
        }
    ]

    def dispatch(self, request,*args, **kwargs):
        group = request.user.groups.filter(user=request.user)[0]
        
        if group.name=="client":
            return redirect('clients:clientlandingpage')

        return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/create.html"
    success_message = "Producto creado exitosamente"

    def form_valid(self, form):
        total_ingredients = 0
        instance = form.instance
        for ingredient in form.cleaned_data['ingredient']:
            total_ingredients += ingredient.price
        instance.price = form.cleaned_data['price'] + total_ingredients
        form.save()
        if not self.request.tenant.plan.custom_products:
            count_products = Product.objects.count()
            if count_products > MAX_PRODUCT_CREATE:
                messages.error(self.request, "Lo sentimos, por favor actualiza tu plan")
                return redirect(reverse("plans:upgrade_plan"))

        if not self.request.tenant.plan.custom_ingredients:
            if form.cleaned_data['ingredient'].count() > 3:
                messages.error(self.request, "Lo sentimos, por favor actualiza tu plan")
                return redirect(reverse("plans:upgrade_plan"))

        return super(ProductCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('products:index')


class ProductUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/update.html"
    success_message = "Producto modificado exitosamente"

    def get_success_url(self):
        return reverse('products:index')


class ProductDeleteView(LoginRequiredMixin, MessageMixin, DeleteView):

    model = Product

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            try:
                plan = get_object_or_404(Product, pk=kwargs['pk'])
                plan.delete()
                return JsonResponse({'status': 1, 'message': 'El Producto fue eliminado con éxito', 'type': 'success'})
            except Exception:
                return JsonResponse({'status': 0, 'message': 'Ha ocurrido un error', 'type': 'error'})


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/detail.html'
