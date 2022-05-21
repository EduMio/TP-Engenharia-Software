from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class Client():
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200) 
    mail = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    business_area = models.CharField(max_length=200,default="Lead")

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True,
    )
    
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    objects = UserManager()

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


class Card():
    responsible = models.CharField(max_length=200) # Email do vendedor responsavel
    description = models.CharField(max_length=2000)
    create_date = models.DateTimeField('date created') # Data de criacao do card
    client_mail = models.CharField(max_length=200)
