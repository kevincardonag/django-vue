from django.utils.translation import ugettext_lazy as _

MENUS = {
    "TENANTS_MENU": [
        {
            "name": _("Ingredientes"),
            "url": "products:list_ingredients",
            "icon": "fas fa-fw fa-hand-holding",
            "validators": [
                #'menu_generator.validators.is_authenticated',
                #('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        },
    ]
}