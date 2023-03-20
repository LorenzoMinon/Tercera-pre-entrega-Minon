from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('cursos/', views.cursoFormulario, name = "Cursos"),
    path('profesores/', views.profesorFormulario, name="Profesores"),
    path('estudiantes/', views.estudianteFormulario, name="Estudiantes"),
    path('entregables/', views.entregableFormulario, name="Entregables"),
    path('cursoFormulario', views.cursoFormulario, name ="CursoFormulario"),
    path('profesorFormulario', views.profesorFormulario, name ="ProfesorFormulario"),
    path('estudianteFormulario', views.estudianteFormulario, name="EstudianteFormulario"),
    path('entregableFormulario', views.entregableFormulario, name="EntregableFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar)

]