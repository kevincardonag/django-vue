from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.utils.translation import ugettext_lazy as _
from django_tenants.utils import get_public_schema_name
from django.db.models import Model

from core.behaviors import ActiveSwitchable
from plans.models import Plan


class Pizzeria(ActiveSwitchable, TenantMixin):
    """
    Modelo que representa las pizzerias como Tenants, hereda de TenantMixin
    """
    name = models.CharField(max_length=100, verbose_name=_("Nombre de la pizzeria"))
    address = models.CharField(max_length=100, verbose_name=_("Dirección de la pizzeria"))
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, null=True, blank=True)
    #department = models.ForeignKey('core.Department', verbose_name=_("Departamento"))
    #city = ChainedForeignKey(City, chained_field='department', chained_model_field='department', show_all=False,verbose_name=_("Ciudad"))
    phones = models.CharField(max_length=100, verbose_name=_("Teléfono(s) de la pizzeria"))
    email = models.EmailField(verbose_name=_("Correo electrónico principal de la pizzeria"),
                              help_text=_("Puede ser el correo del notario"))
    logo = models.ImageField(upload_to="pizzeria_logos/", blank=True, null=True, verbose_name=_("Logo de la pizzeria"))
    #subdomain = models.CharField(max_length=50, unique=True, verbose_name=_("Subdominio"))

    auto_create_schema = True
    auto_drop_schema = True

    has_physical_delivers = models.BooleanField(default=True, verbose_name=_("¿Acepta envíos físicos?"))

    def is_public(self):
        return self.schema_name == get_public_schema_name()

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    """
    Modelo que representa al dominio de los tenants
    """
    pass

    def __str__(self):
        return self.domain


class PizzeriaRequest(Model):
    is_active = models.BooleanField(verbose_name=_("Solicitud activa"), default=True)
    representative_full_name = models.CharField(
        max_length=100,
        verbose_name=_("Nombre completo representante legal"),
        null=True
    )
    phone = models.CharField(max_length=10, verbose_name=_("Telefono representante legal"))
    email = models.EmailField(max_length=100, verbose_name=_("Email representante legal"))
    comment = models.TextField(max_length=3000, verbose_name=_("Comentario"))
    company_name = models.CharField(max_length=10, verbose_name=_("Nombre de la compañia"), null=True)
    address = models.CharField(max_length=100, verbose_name=_("Dirección de la pizzeria"), null=True)
    plan = models.ForeignKey(Plan, null=True, on_delete=models.CASCADE)

