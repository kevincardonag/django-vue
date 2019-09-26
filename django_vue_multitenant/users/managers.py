from django.contrib.auth.models import UserManager


class UserProfileManager(UserManager):
    """
    Manager para controlar el modelo de usuarios que se creo, esto es requerido por AbstractBaseUser de django
    """

    def create_user(self, email, password=None, **kwargs):
        """
        :param email: email del usuario
        :param password: contraseña (si se requiere)
        :param kwargs: parametros adicionales
        :return: usuario creado
        """
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Método para crear un superusuario
        :param email: email del superusuario
        :param password: contraseña (si se requiere)
        :param kwargs: parametros adicionales
        :return: superusuario creado
        """
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user
