# django-vue
Repositorio de aplicación multitenant para pizzerias django and vue project

Desarrollado por: Grupo de tendecias de software de la universidad del Valle 

Desarrolladores:

Kevin Cardona
Carlos Almario

Instrucciones de instalación:
Clonar el repositorio.

Crear una base de datos en PostgreSQL con las credenciales especificadas en el settings.

Crear un virtualenv, para mayor comodidad se recomienda utilizar virtualenvwrapper.

Instalar los requirements en el virtualenv:

pip install -r requirements.txt
Crear las migraciones:

python manage.py makemigrations
Correr las migraciones, OJO: para multitenant se debe correr migrate_schemas en vez de migrate:

python manage.py migrate_schemas
Cargar los archivos .sql contenidos en el directorio data_and_scripts

Correr el siguiente comando el cual creará un tenant público con un usuario por defecto (email: desarrollo1@radyconsultores.com, password: rady1234), a la vez actualiza los permisos, grupos y notificaciones:

python manage.py shell < data_and_scripts/initial_setup.py
Ingresar a la carpeta data_and_scripts y sincronizar todos los archivos .sql en la base de datos