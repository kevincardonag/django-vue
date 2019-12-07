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
from django.http.response import JsonResponse

from tenants.mixins import UserPermissionMixin
from orders.forms import OrderForm
from orders.models import Order

# Create your views here.

class OrdertListView(LoginRequiredMixin, UserPermissionMixin, TemplateDataMixin, DatatablesListView):
    model = Order
    page_title = _("Ordenes")
    section_title = _("Listado de Ordenes")
    model_name = _("Ordenes")
    fields = ["client_name", "direction", "payment_method", "price_products", "state"]
    # create_reversible_url = 'orders:create_product'
    class_modal_create = "ajax-modal-large"
    column_names_and_defs = [_("Cliente"), _("Direccion"), _("Metodo pago"), _("Precio"), _("Estado"),]
    options_list = [
        {
            "label_opcion": _('Editar'),
            "url_opcion": 'orders:update_order',
            "parametros_url": ["id"],
            "icono": 'fa-pencil-alt',
            "confirm_modal": 'ajax-base-modal-large',
            "class_target_modal": 'ajax-modal-large'
        },
        {
            "label_opcion": _('Consultar'),
            "url_opcion": 'orders:detail',
            "parametros_url": ["id"],
            "icono": 'fa-eye',
            "confirm_modal": 'ajax-base-modal-large',
            "class_target_modal": 'ajax-modal-large'
        },
        # {
        #     "label_opcion": _('Eiminar'),
        #     "url_opcion": "products:delete_product",
        #     "parametros_url": ["id"],
        #     "icono": 'fa-trash',
        #     "object_modal_delete": 'dd',
        # }
    ]

class OrderUpdateView(LoginRequiredMixin, UserPermissionMixin, MessageMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/update.html"
    success_message = "Orden modificada exitosamente"

    def get_success_url(self):
        return reverse('orders:index')

class OrderDetailView(LoginRequiredMixin, UserPermissionMixin, DetailView):
    model = Order
    template_name = 'orders/detail.html'