from django.utils.translation import ugettext_lazy as _

MENUS = {
    "TENANTS_MENU": [
        {
            "name": _("Usuarios"),
            "url": "users:index",
            "icon": " fas fa-users",
            "validators": [
                'menu_generator.validators.is_authenticated',
                #('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        },
        {
            "name": _("Ingredientes"),
            "url": "products:list_ingredients",
            "icon": "fas fa-fw fa-hand-holding",
            "validators": [
                'menu_generator.validators.is_authenticated',
                #('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        },
        {
            "name": _("Productos"),
            "url": "products:index",
            "icon": "fas fa-fw fa-hand-holding",
            "validators": [
                'menu_generator.validators.is_authenticated',
                #('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        },
        {
            "name": _("Actualizar plan"),
            "url": "plans:upgrade_plan",
            "icon": " fas fa-hand-holding",
            "validators": [
                'menu_generator.validators.is_authenticated',
                #('menu_generator.validators.user_has_permission', "tenants.list_pizzerias"),
            ]
        },

    ]
}