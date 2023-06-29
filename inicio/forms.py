from django import forms


class CrearAlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    curso = forms.IntegerField()
    division = forms.CharField(max_length=1)