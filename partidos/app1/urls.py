from django.urls import path
from .views import ListaPartidos
from . import views

urlpatterns = [
    path('partidos/', ListaPartidos.as_view(), name='lista_partidos'),
    #path('', views.home, name='home'),
    path('api/partidos/', views.ListaPartidos.as_view(), name='lista_partidos_api'),
    path('', views.partidos_view, name='partidos_view'),  # Ruta para la plantilla HTML
    path('api/partidos/', views.ListaPartidos.as_view(), name='lista_partidos_api'),
   
]
