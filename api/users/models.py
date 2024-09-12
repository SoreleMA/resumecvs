from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email Field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser, PermissionsMixin):

    # Sobrescribir el campo 'username' para eliminarlo
    username = None 
    
    ROLES = (
        ('admin', 'Administrador'),
        ('user', 'cliente'),
        ('company', 'empresa'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name} ({self.email})'

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_company(self):
        return self.role == 'company'

    @property
    def is_client(self):
        return self.role == 'client'