<<<<<<< HEAD
from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
from django.contrib.auth.models import User

'''
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test


>>>>>>> 5137fd2 (Actualización)
def registro(request):
    datos = ''
    errors = []

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        datos = request.POST

        # Validacion basica
        if password1 != password2:
            errors.append('Las contraseñas no coinciden')

        if User.objects.filter(username=username).exists():
            errors.append('El nombre de usuario ya existe')

        if User.objects.filter(email=email).exists():
            errors.append('El correo electronico ya esta registrado')

        if not errors:
            # Create _user hashea la contraseña automaticamente
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            return redirect('home')
<<<<<<< HEAD
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
'''

def registro(request):
    datos = ''
    errors = []

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        datos = request.POST

        if password1 != password2:
            errors.append('Las contraseñas no coinciden.')

        if User.objects.filter(username=username).exists():
            errors.append('El nombre de usuario ya existe.')

        if User.objects.filter(email=email).exists():
            errors.append('El correo electrónico ya está registrado.')

        if not errors:
            # create_user hashea la contraseña auto
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            return redirect('home')

    return render(request, 'registro.html', {'errors':errors, 'datos':datos}) 
=======
    return render(request, 'registro.html', {'errors':errors, 'datos': datos})

def es_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(es_admin)
def grupos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre').strip()
        if nombre and not Group.objects.filter(name=nombre).exists():
            Group.objects.create(name= nombre)
        return redirect('grupos')
        
    grupos = Group.objects.all()

    return render(request, 'grupos.html', {'grupos': grupos})

@user_passes_test(es_admin)
def eliminar_grupo(request, id_grupo):
    if request.method == 'POST':
        grupo = get_object_or_404(Group, id=id_grupo)
        grupo.delete()
    return redirect('grupos')

def editar_grupo(request, id_grupo):
    grupo = Group.objects.get(id=id_grupo)

    if request.method == "POST":
        nombre = request.POST.get('nombre')

        # print(nombre,descripcion, duracion) Imprime en la terminal

        if nombre:
            grupo.name = nombre

            grupo.save()

            return redirect('grupos')

    return render(request, 'editar-grupo.html', {'grupo': grupo})
>>>>>>> 5137fd2 (Actualización)
