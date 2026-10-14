from django.db import models

# Create your models here.

class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.IntegerField()
    email = models.EmailField(unique=True)
    telefono = models.IntegerField(unique=True)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.rut} {self.nacionalidad}"

class Billete(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=120)
    asiento = models.IntegerField()
    fecha_ida = models.DateField()
    fecha_vuelta = models.DateField()
    pasajero = models.ForeignKey('Pasajero', on_delete=models.PROTECT)
    vuelo = models.ForeignKey('Vuelo', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.origen} {self.destino} {self.asiento} {self.fecha_ida} {self.fecha_vuelta}"

class Piloto(models.Model):
    nombre_piloto = models.CharField(max_length=100)
    apellido_piloto = models.CharField(max_length=100)
    rut = models.IntegerField()
    telefono = models.IntegerField()
    vuelos = models.ManyToManyField('Vuelo')

    def __str__(self):
        return f"{self.nombre_piloto} {self.apellido_piloto} {self.telefono} {self.rut}"

class Aeropuerto(models.Model):
    nombre_aeropuerto = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_aeropuerto} {self.ubicacion}"
    
class Vuelo(models.Model):
    codigo_vuelo = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    fecha_llegada = models.DateField()
    aeropuerto = models.ForeignKey('Aeropuerto', on_delete=models.PROTECT)
    avion = models.ForeignKey('Avion', on_delete=models.PROTECT)
    aerolinea = models.ForeignKey('Aerolinea', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.codigo_vuelo} {self.fecha_salida} {self.fecha_llegada}"

class Avion(models.Model):
    matricula = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    anio_fabricacion = models.IntegerField()
    activo = models.CharField(max_length=2)
    fabricante = models.ForeignKey('Fabricante', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.matricula} {self.modelo} {self.capacidad} {self.anio_fabricacion} {self.activo}"

class Fabricante(models.Model):
    sucursal = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.sucursal} {self.telefono} {self.email}"

class Aerolinea(models.Model):
    nombre_aerolinea = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_aerolinea