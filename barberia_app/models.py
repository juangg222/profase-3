from django.db import models
from django.db import models

class Barbero(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    correo_electronico = models.EmailField(max_length=100, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
   
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Barbero"
        verbose_name_plural = "Barberos"
        db_table = "barbero"
        ordering = ['id']


class Servicio(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.PositiveIntegerField(verbose_name="Precio")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        db_table = "servicio"
        ordering = ['id']


class Formulario(models.Model):
    nombre_cliente = models.CharField(max_length=30, verbose_name="Nombre del Cliente")
    servicios = models.ManyToManyField('Servicio', verbose_name="Servicios")
    correo = models.EmailField(max_length=100, verbose_name="Correo Electrónico", null=True, blank=True)  # Permitir NULL y vacío temporalmente
    dia_hora = models.DateTimeField(verbose_name="Día y Hora")
    total = models.PositiveIntegerField(verbose_name="Total", default=0)

    def __str__(self):
        return self.nombre_cliente

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"
        db_table = "formulario"
        ordering = ['id']


class Cita(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    estado = models.CharField(max_length=20, verbose_name="Estado")
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE, verbose_name="Barbero")
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, verbose_name="Formulario")
    servicios = models.ManyToManyField(Servicio, verbose_name="Servicios")

    def __str__(self):
        return f"Cita con {self.barbero.nombre} el {self.fecha}"

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        db_table = "cita"
        ordering = ['id']


class Pago(models.Model):
    monto = models.PositiveIntegerField(verbose_name="Monto")
    metodo = models.CharField(max_length=20, verbose_name="Método")
    fecha = models.DateField(verbose_name="Fecha")
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, verbose_name="Cita")

    def __str__(self):
        return f"Pago de {self.monto} para la cita {self.cita.id}"

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        db_table = "pago"
        ordering = ['id']