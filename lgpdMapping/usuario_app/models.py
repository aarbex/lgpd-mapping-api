import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):

    def create_user(self, nome, username, email, perfil, password=None, **kwargs):
        if username is None:
            raise TypeError('Usuários devem ter um username')
        if email is None:
            raise TypeError('Usuários devem ter um e-mail')

        user = self.model(nome=nome, username=username, email=self.normalize_email(email), perfil=perfil, password = password, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, nome, username, email, perfil, password):
        if password is None:
            raise TypeError('Uma senha deve ser definida')
        perfil_id = Perfil.objects.get(id=perfil)



        user = self.create_user(nome, username,  email, perfil_id, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Perfil(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100, db_index=True)
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=50, unique=True, db_index=True)
    perfil = models.ForeignKey(Perfil, related_name='perfil', on_delete=models.PROTECT)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nome', 'username', 'perfil']

    objects = UserManager()

    def __str__(self):
        return self.nome

    def tokens(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    class Meta:
        ordering = ['nome']
        


