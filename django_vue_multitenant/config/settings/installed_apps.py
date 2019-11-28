# Application definition
SHARED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django_tenants',
    # 'django_restframework',
    'rest_framework',
    'bootstrap3',
    'webpack_loader',
    'users',
    'core',
    'api_rest',
    'tenants',
    'menu_generator',
    "parsley",
    "plans",

]

TENANT_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'webpack_loader',
    'users',
    "products",
    "client",
    "social_django",
]

INSTALLED_APPS = SHARED_APPS + [app for app in TENANT_APPS if app not in SHARED_APPS]


