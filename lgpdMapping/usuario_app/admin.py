from django.contrib import admin
from usuario_app.models import Usuario, Perfil
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    model = Usuario
    search_fields = ('nome', 'username', 'email', 'perfil',)
    list_filter = ('nome','username', 'email', 'perfil', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('nome',)
    list_display = ('nome','username', 'email', 'perfil', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, { 'fields': ('nome', 'username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('nome','username', 'email', 'perfil', 'password1', 'password2', 'is_active', 'is_staff',)
        }),
    )

admin.site.register(Usuario, UserAdminConfig)
admin.site.register(Perfil)
