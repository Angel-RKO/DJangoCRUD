from django.urls import path
# Vamos a tener acceso a las vistas y a cual la vamos a redirigir
from . import views

urlpatterns = [
    # Traemos el view de la funcion inicio desde views.py
    path('',views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('libros/',views.libros,name="libros"),
]
