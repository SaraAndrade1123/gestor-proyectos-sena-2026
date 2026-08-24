# Entornos virtual
Entorno de aislamiento, con portabilidad y un control de versiones

**Sí**, __No__, *Cat*, _Kitty_, ~~Jojo's~~,`A ya`

python3 -m venv my_melody_house

## Activar entorno virtual

source my_melody_house/bin/activate

pip list
Listado de las dependencias instaladas en el entorno virtual

pip install django
Instalar django

django-admin --version

django-admin startproject Sara .
Carpeta al mismo nivel del entorno virtual, con el punto que crea el proyecto en la misma carpeta en la que se encuentra

python3 manage.py runserver

lambda es una función sin nombre

from django.http import HttpResponse
from . import views
 path('',lambda request: HttpResponse("¡Hola mundo desde Django!")),
    path('acerca-de/', views.about_us),
    
    
VIEWS.PY

from django.http import HttpResponse

def about_us(request):
    return HttpResponse("Acerca de nosotros holla.")
    
Épica, conjunto de historias de usuario

python3 manage.py startapp gestor_proyectos

Desactivar entorno virtual

deactivate

renderizar, que se muestre o genere algo visual, renderizar una web

python3 manage.py makemigrations
python manage.py migrate
