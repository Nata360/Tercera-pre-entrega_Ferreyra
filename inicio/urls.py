from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alumnos/crear/', views.crear_alumno, name='crear_alumno'),
]
