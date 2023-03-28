from django.shortcuts import render
from AppCoder.models import Curso,Profesor,Estudiantes,Entregable
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario,ProfesorFormulario,EstudianteFormulario,EntregableFormulario

# Create your views here.

""" def curso(self):
    
    curso = Curso(nombre="Desarrollo Web", camada = "20000")
    curso.save()
    documentoDeTexto = f"---> Curso:  {curso.nombre} Camada: {curso.camada} "

    return HttpResponse(documentoDeTexto)
 """

def inicio(request):
    return render(request,'AppCoder/inicio.html')

def cursos(request):
    return render(request,'AppCoder/cursoFormulario.html')

def profesores(request):
    return render(request,'AppCoder/profesorFormulario.html')

def estudiantes(request):
    return render(request,'AppCoder/estudianteFormulario.html')

def entregables(request):
    return render(request,'AppCoder/entregableFormulario.html')

def cursoFormulario(request):

    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST) # Directo del post del html
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            curso = Curso(nombre = informacion["curso"], camada=informacion["camada"])
            
            curso.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def profesorFormulario(request):

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST) # Directo del post del html
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre = informacion["nombre"], apellido=informacion["apellido"], email= informacion["email"], profesion=informacion["profesion"])
            
            profesor.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProfesorFormulario()

    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})

def estudianteFormulario(request):

    if request.method == "POST":

        miFormulario = estudianteFormulario(request.POST) # Directo del post del html
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            estudiante = Estudiante(nombre = informacion["nombre"], apellido=informacion["apellido"], email= informacion["email"])
            
            estudiante.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EstudianteFormulario()

    return render(request, "AppCoder/estudianteFormulario.html", {"miFormulario":miFormulario})

def entregableFormulario(request):

    if request.method == "POST":

        miFormulario = EntregableFormulario(request.POST) # Directo del post del html
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            entregable = Entregable(nombre = informacion["nombre"], fechaDeEntrega=informacion["fechaDeEntrega"], entregado=informacion["entregado"])
            
            entregable.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EntregableFormulario()

    return render(request, "AppCoder/entregableFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    #respuesta = f"Buscando camada número: {request.GET['camada'] }"
    if request.GET["camada"]:

        camada = request.GET['camada']

        cursos = Curso.objects.filter(camada__icontains=camada)



        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos":cursos, "camada":camada})

    else:
        
        respuesta = "No se han enviado datos"

    return HttpResponse(respuesta)

def leerProfesores(request):

    profesores = Profesor.objects.all() #traemos a todos los profesores

    contexto = {"profesores":profesores}

    return render(request, "AppCoder/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    #volvemos al menu

    profesores = Profesor.objects.all() #traemos todos de nuevo

    contexto = {"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST) # nos llega la info del html

        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data

            profesor.nombre = informacion('nombre')
            profesor.apellido = informacion('apellido')
            profesor.email = informacion('email')
            profesor.profesion = informacion('profesion')

            profesor.save()

            return render(request, "AppCoder/inicio.html")


    else: #en caso de que no sea un post

        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre,'apellido':profesor.apellido,'email':profesor.email,'profesion':profesor.profesion})

    return render(request, "AppCoder/editarProfesor.html",{"miFormulario":miFormulario,"profesor_nombre":profesor_nombre})