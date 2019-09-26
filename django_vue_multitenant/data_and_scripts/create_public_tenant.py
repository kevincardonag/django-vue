"""
Mediante este script se puede crear el tenant público después de migrar por primera vez la aplicación, es indispensable
para el funcionamiento del multitenant
"""
from django.conf import settings
from django.contrib.sites.models import Site

from tenants.models import Pizzeria, Domain
from users.models import UserProfile

# Creación tenant público
tenant = Pizzeria.objects.create(schema_name='public', name='public', address='public', phones='public',
                                email='public@public.co')

# Se actualiza los datos del dominio
domain = settings.DOMAIN

if hasattr(settings, "SUBDOMAIN"):
    domain = "{0}.{1}".format(settings.SUBDOMAIN, domain)

if settings.PORT:
    domain = "{0}:{1}".format(domain, settings.PORT)

site = Site.objects.filter(id=settings.SITE_ID).update(domain=domain, name=settings.PRODUCT_NAME)

# Dominio del tenant
Domain.objects.create(domain=settings.DOMAIN, tenant=tenant)

# Usuario del tenant
user = UserProfile.custom_objects.create_user(email='admin@admin.com', password='admin1234', first_name='admin',
                                       last_name='admin', is_superuser=True)
