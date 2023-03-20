from django import forms


class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField() #curso
    camada = forms.IntegerField() #camada

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email=  forms.EmailField(max_length=30)
    profesion=  forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()