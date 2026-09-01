from django.db import models

# Create your models here.
class Proyecto(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    nombre = models.CharField(max_length=100) # campo de texto (varchar)
    descripcion = models.TextField() # Campo de texto largo
    duracion = models.IntegerField() # Campo numérico entero

    imagen = models.ImageField(upload_to='img/', default='img/michi.png')

    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    '''
    Modelo que representa una tarea de un proyecto
    '''

    PRIORIDAD_CHOICES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    ]

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
    ]

    # Cardinalidad/ relacion
    # Relación de 1 a muchos/varios: Un proyectoo tiene muchas tareas
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='tareas',
    )

    titulo= models.CharField(max_length=50)
    prioridad=models.CharField(max_length=5, choices=PRIORIDAD_CHOICES, default='MEDIA')
    estado=models.CharField(max_length=12, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
            return self.titulo + '(' + self.proyecto.nombre + ')'