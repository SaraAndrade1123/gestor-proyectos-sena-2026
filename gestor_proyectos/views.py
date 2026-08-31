from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Proyecto, Tarea

# Create your views here.
def home(request):
    return render(request, 'home.html')

def acerca_de(request):
    return render(request, 'acerca-de.html')

def mostrar_proyectos0(request):
    proyectos = Proyecto.objects.all()

    nombres_proyectos = list()

    for p in proyectos:
        nombres_proyectos.append(p.nombre)

        respuesta = '<br>'.join(nombres_proyectos)

    return HttpResponse(respuesta)

def mostrar_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request,'proyectos.html', {'proyectos': proyectos})

def nuevo_registro(request):
    Proyecto.objects.create(nombre= 'SOE', descripcion= 'Software del observador del estudiante en una I.E.', duracion=832)

    return HttpResponse('- 😸 Registro guardado!! 𖹭⋆˚࿔')

    '''
    ** En SQL **

    INSERT INTO proyecto (nombre, descripcion, duracion) VALUES ("Aplicacion de biblioteca", "Apliación web para gestionar los libros y préstamos de la biblioteca", 200)
    '''

# def ver_producto(request, id):
#     return HttpResponse(f'Producto id: {id}! 🎀')

def ver_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id) #el id que se le coloca en la url
    print(proyecto.tareas.all)

    # return redirect('ver_proyecto.html', id: proyecto)
    return render(request, 'detalle-proyecto.html', {'proyecto': proyecto})

def nuevo_proyecto(request):

    if request.method == "POST":

        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')
        imagen = request.FILES.get('imagen')

        if nombre and descripcion and duracion:
            proyecto = Proyecto(
                nombre=nombre,
                descripcion=descripcion,
                duracion=int(duracion),
                imagen = imagen,
            )

            proyecto.save()

            return redirect('proyectos') 

    return render(request, 'nuevo-proyecto.html')

'''
def crear_proyecto(request):
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    duracion = request.POST.get('duracion')

    if nombre and descripcion and duracion:
        proyecto = Proyecto(
            nombre=nombre,
            descripcion=descripcion,
            duracion=int(duracion),
        )

        proyecto.save()

        return redirect('proyectos')

    return render(request, 'nuevo-proyecto.html')
'''

def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('proyectos')

def editar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')

        # print(nombre,descripcion, duracion) Imprime en la terminal

        if nombre and descripcion and duracion:
            proyecto.nombre = nombre
            proyecto.descripcion = descripcion
            proyecto.duracion = int(duracion)

            proyecto.save()

            return redirect('ver_proyecto', id=proyecto.id)

    return render(request, 'editar-proyecto.html', {'proyecto': proyecto})


# TAREAS

def crear_tarea(request,proyecto_id):
    proyecto=get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == "POST":
        titulo = request.POST.get('titulo').strip()
        prioridad = request.POST.get('prioridad')
        estado = request.POST.get('estado')

        if titulo:
            tarea = Tarea(
                titulo= titulo, 
                prioridad= prioridad, 
                estado=estado, 
                proyecto= proyecto)
            
            tarea.save()

            return redirect('ver_proyecto', id=proyecto_id)

    datos = {
        'proyecto': proyecto,
        'prioridad_choices': Tarea.PRIORIDAD_CHOICES,
        'estado_choices':Tarea.ESTADO_CHOICES,
    }

    return render(request, 'crear-tarea.html', datos)

@require_POST

def avanzar_estado_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if tarea.estado == 'PENDIENTE':
        tarea.estado = 'EN_PROGRESO'
        tarea.save()

    elif tarea.estado == 'EN_PROGRESO':
        tarea.estado = 'COMPLETADA'
        tarea.save()


    return redirect('ver_proyecto', id=tarea.proyecto.id)

def terminar_estado_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if tarea.estado == 'PENDIENTE':
        tarea.estado = 'COMPLETADA'
        tarea.save()

    elif tarea.estado == 'EN_PROGRESO':
        tarea.estado = 'COMPLETADA'
        tarea.save()

@require_POST
def eliminar_tarea(request, id):
    tarea = get_object_or_404(id=id)

    id_proyecto = tarea.proyecto.id

    tarea.delete()
    return redirect('ver_proyecto', id=id_proyecto)