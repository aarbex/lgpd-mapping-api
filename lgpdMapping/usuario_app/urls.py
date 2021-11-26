from django.urls import path
from usuario_app.views import usuario_list, usuario_by_id, usuario_create, usuario_update, usuario_delete, perfil_list, perfil_by_id, perfil_create, perfil_update, perfil_delete


urlpatterns = [
    path('/', usuario_list, name='listar-usuarios'),
    path('/<int:pk>', usuario_by_id, name='usuario-by-id'),
    path('/create', usuario_create, name='create_user'),
    path('/update/<int:pk>', usuario_update, name='usuario-update'),
    path('/delete/<int:pk>', usuario_delete, name='usuario-delete'),
    # Perfil de Usuário
    path('/perfil', perfil_list, name='listar-perfis'),
    path('/perfil/<int:pk>', perfil_by_id, name='perfil-by-id'),
    path('/perfil/create', perfil_create, name='perfil-create'),
    path('/perfil/update/<int:pk>', perfil_update, name='perfil-update'),
    path('/perfil/delete/<int:pk>', perfil_delete, name='perfil-delete'),
    # path('/register', RegistrationAPIView.as_view()),
    # path('/login', LoginAPIView.as_view()),
]