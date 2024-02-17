from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import Login, Registro, ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea


urlpatterns = [
    path('', ListaPendientes.as_view(), name='tareas'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('tarea/<int:pk>/', DetalleTarea.as_view(), name='ver_tarea'),
    path('tarea/crear/', CrearTarea.as_view(), name='crear_tarea'),
    path('tarea/editar/<int:pk>/', EditarTarea.as_view(), name='editar_tarea'),
    path('tarea/eliminar/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
]
