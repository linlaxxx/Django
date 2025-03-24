from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Reparacion(models.Model):
    ESTATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    estatus = models.CharField(max_length=10, choices=ESTATUS_CHOICES, default='pendiente')
    detalles_equipo = models.TextField()
    descripcion_equipo = models.TextField()

    def __str__(self):
        return f"Reparación #{self.id} - {self.cliente.nombre}"

