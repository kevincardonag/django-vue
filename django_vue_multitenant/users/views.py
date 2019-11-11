from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import PasswordChangeView, PasswordResetView

from core.datatables_tools.datatables_tools import DatatablesListView
from core.mixins import MessageMixin, TemplateDataMixin
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from users.models import UserProfile
from .forms import UserForm
from django.utils.translation import ugettext as _


class CustomPasswordChangeView(MessageMixin, PasswordChangeView):
    success_message = 'La contraseña se actualizó correctamente'

    def get_success_url(self):
        return reverse('login')


class CustomPasswordResetView(MessageMixin, PasswordResetView):
    success_message = 'El link para recuperar tu contraseña ha sido enviado a tu correo'

    def get_success_url(self):
        return reverse('login')


class UsersListView(LoginRequiredMixin, TemplateDataMixin, DatatablesListView):

    """
        Autor: Caros Almario
        Fecha: Septiembre 29 2019
        Vista para lisar las solicutdes de las franquicias
    """
    model = UserProfile
    queryset = None
    page_title = _("Usuarios")
    section_title = _("Listado de Usuarios")
    model_name = _("Usuario")
    create_reversible_url = 'users:create'
    fields = ["first_name", "last_name", "email"]
    class_modal_create = "ajax-modal-large"
    column_names_and_defs = [_("Nombre"), _("Apellido"), _("Correo")]
    options_list = [
        {
            "label_opcion": _('Editar'),
            "url_opcion": 'users:update',
            "parametros_url": ["id"],
            "icono": 'fa-pencil-alt',
            "confirm_modal": 'ajax-base-modal-large',
            "class_target_modal": 'ajax-modal-large'
        },
        {
           "label_opcion": _('Consultar'),
           "url_opcion": 'users:detail',
           "parametros_url": ["id"],
           "icono": 'fa-eye',
           "confirm_modal": 'ajax-base-modal',
        },
        {
           "label_opcion": _('Eiminar'),
           "url_opcion": "users:delete",
           "parametros_url": ["id"],
           "icono": 'fa-trash',
           "object_modal_delete": 'dd',
        }
    ]


class UsersCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = UserProfile
    form_class = UserForm
    template_name = 'users/create.html'
    success_message = 'El usuario se creó exitosamente'

    def get_success_url(self):
        return reverse('users:index')

    def form_valid(self, form):
        user = form.instance
        user.set_password(form.cleaned_data['password'])
        user.save()
        group = form.cleaned_data['group']
        user.groups.add(group)
        return super(UsersCreateView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = UserProfile
    form_class = UserForm
    template_name = 'users/update.html'
    success_message = "El usuario se modificó exitosamente"

    def get_success_url(self):
        return reverse('users:index')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'users/detail.html'


class UserDeleteView(LoginRequiredMixin, MessageMixin, DeleteView):
    model = UserProfile
    delete_message = "Usuario eliminado con éxito"

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            try:
                user = get_object_or_404(UserProfile, pk=kwargs['pk'])
                user.delete()
                return JsonResponse({'status': 1, 'message': 'El Usuario fue eliminado con éxito', 'type': 'success'})
            except Exception:
                return JsonResponse({'status': 0, 'message': 'Ha ocurrido un error', 'type': 'error'})
