from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#Formulario para crear usuarios
class UserCreationForm(ModelForm):

    class Meta:
        model = User
        fields = ('email', 'name', 'role')

def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    if commit:
        user.save()
    return user

#Formulario para actualizar usuarios
class UserChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'role', 'is_active', 'is_staff')

#Formulario para agregar y cambiar usuarios

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

#Los Campos a mostrar en el panel de administración

    list_display = ('email', 'name', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('Informacion Personal', {'fields': ('name', 'role')}),
        ('Permisos', {'fields': ('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'role')
        }),
    )

    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()

# Register your models here.
admin.site.register(User, UserAdmin)
