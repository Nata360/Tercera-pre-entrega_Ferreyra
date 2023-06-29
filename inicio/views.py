from django.shortcuts import render
from django.http import HttpResponse
from inicio.forms import CrearAlumnoForm
from inicio.models import CrearAlumno
# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_alumno(request):
    
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearAlumnoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = CrearAlumno(nombre=info['nombre'],apellido=info['apellido'], curso=info['curso'], division=info['division'] )
            alumno.save()
            mensaje = f'Se ha completado la inscripción de {alumno.nombre} en {alumno.curso}, "{alumno.division}" correctamente.'
        else:
            return render(request, 'inicio/crear_alumno.html', {'formulario': formulario})
            
    formulario = CrearAlumnoForm()
    return render(request, 'inicio/crear_alumno.html', {'formulario': formulario, 'mensaje':mensaje})