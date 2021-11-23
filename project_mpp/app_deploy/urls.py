from django.urls import path
from .views import SelectTrabajadorController

urlpatterns= [
    path("buscar-trabajador/", SelectTrabajadorController.as_view())
]
