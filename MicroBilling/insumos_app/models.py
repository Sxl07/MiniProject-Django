from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    unidad_medida = models.CharField(max_length=50)
    precio = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    OPCIONES = [
        ('pagado', 'PAGADO'),
        ('pendiente', 'PENDIENTE'),
        ('cancelado', 'CANCELADO'),
    ]
    estado = models.CharField(max_length=50, choices=OPCIONES)

    def __str__(self):
        return f"Pedido de {self.insumo} - Cantidad: {self.cantidad} - Fecha: {self.fecha_pedido}"
