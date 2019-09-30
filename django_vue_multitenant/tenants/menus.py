from django.utils.translation import ugettext_lazy as _

MENUS = {
    "NAV_MENU_LEFT": [
        {
            "name": _("Solicitudes"),
            "url": "tenants:request_tenant",
            "icon": "fas fa-fw fa-hand-holding",
            "validators": [
                'menu_generator.validators.is_authenticated',
                ('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        },
        {
            "name": _("Pizzerías"),
            "url": "tenants:index",
            "icon": "fas fa-fw fa-store-alt",
            "validators": [
                'menu_generator.validators.is_authenticated',
                ('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        },
        {
            "name": _("Planes"),
            "url": "plans:index",
            "icon": "fas fa-fw fa-credit-card",
            "validators": [
                'menu_generator.validators.is_authenticated',
                ('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        }
    ]
}
