from django.utils.translation import ugettext_lazy as _

MENUS = {
    "TENANTS_MENU": [
        {
            "name": _("Reportes"),
            "url": "reports:index",
            "icon": " fas fa-file-alt",
            "validators": [
                'menu_generator.validators.is_authenticated',
                #('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ],

        },
    ]
}

