from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
   #rota, views resposável, nome de referÊncia
   #usuarios.com
   path("", views.home,name="home"),
   #usuarips.com/usuarios
   path("usuarios/", views.usuarios, name="Listagem_usuarios")
]
