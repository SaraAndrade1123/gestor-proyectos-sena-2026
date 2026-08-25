from django.http import HttpResponse
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('proyectos/', views.mostrar_proyectos, name='proyectos'),
    # path('proyectos0/', views.mostrar_proyectos0),
    path('nuevo-registro/', views.nuevo_registro, name='nuevo_registro'),

    # path('productos/<int:id>/', views.ver_producto, name='ver_producto'),

    path('proyectos/<int:id>/', views.ver_proyecto, name='ver_proyecto'),

    path('proyectos/nuevo/', views.nuevo_proyecto, name='nuevo_proyecto'),
    
    # path('proyectos/crear_proyecto/', views.crear_proyecto, name='crear_proyecto'), manejarlo todo con una sola URL

    path('proyectos/<int:id>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),

    path('proyectos/<int:id>/editar/', views.editar_proyecto, name='editar_proyecto'),

    path("proyectos/<int:proyecto_id>/tareas/nueva/", views.crear_tarea, name="crear_tarea"),

    path("tareas/<int:id>/avanzar/", views.avanzar_estado_tarea, name="avanzar_estado_tarea"),

    path("tareas/<int:id>/terminar/", views.terminar_estado_tarea, name="terminar_estado_tarea"),

    path('tareas/<int:id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]