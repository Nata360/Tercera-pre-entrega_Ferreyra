from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.forms import CrearAlumnoForm, BuscarAlumnoApellidoForm
from inicio.models import CrearAlumno
# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_alumno(request):
    
    
    if request.method == 'POST':
        formulario = CrearAlumnoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = CrearAlumno(nombre=info['nombre'],apellido=info['apellido'], curso=info['curso'], division=info['division'] )
            alumno.save()

            return redirect('inicio:lista_alumnos')
        else:
            return render(request, 'inicio/crear_alumno.html')
            
    formulario = CrearAlumnoForm()
    return render(request, 'inicio/crear_alumno.html', {'formulario': formulario})

def lista_alumnos(request):
    formulario = BuscarAlumnoApellidoForm(request.GET)
    if formulario.is_valid():
        apellido_a_buscar = formulario.cleaned_data['apellido']
        listado_de_alumnos = CrearAlumno.objects.filter(apellido__icontains=apellido_a_buscar)
    
    formulario = BuscarAlumnoApellidoForm()
    return render(request, 'inicio/lista_alumnos.html', {'formulario': formulario, 'alumnos': listado_de_alumnos})