from django.utils.translation import ugettext_lazy as _

MENUS = {
    "NAV_MENU_LEFT": [
        {
            "name": _("Pizzerías"),
            "url": "tenants:tenant_list",
            "icon": "fa-bank",
            "validators": [
                'menu_generator.validators.is_authenticated',
                ('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        }
    ]
}
