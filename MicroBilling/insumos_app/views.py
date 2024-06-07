from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Insumo
from .forms import InsumoForm
from .models import Proveedor
from .forms import ProveedorForm
from .models import Pedido
from .forms import PedidoForm


@login_required
def lista_insumos(request):
    insumos = Insumo.objects.all()
    return render(request, 'lista_insumos.html', {'insumos': insumos})
@login_required
def detalle_insumo(request, insumo_id):
    insumo = Insumo.objects.get(pk=insumo_id)
    return render(request, 'detalle_insumo.html', {'insumo': insumo})
@login_required
def crear_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_insumos')
    else:
        form = InsumoForm()
    return render(request, 'crear_insumo.html', {'form': form})
@login_required
def editar_insumo(request, insumo_id):
    insumo = get_object_or_404(Insumo, pk=insumo_id)
    if request.method == 'POST':
        form = InsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            return redirect('lista_insumos')
    else:
        form = InsumoForm(instance=insumo)
    return render(request, 'editar_insumo.html', {'form': form})
@login_required
def eliminar_insumo(request, insumo_id):
    insumo = get_object_or_404(Insumo, pk=insumo_id)
    if request.method == 'POST':
        insumo.delete()
        return redirect('lista_insumos')
    return render(request, 'confirmar_eliminacion.html', {'insumo': insumo})


@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})
@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})
@login_required
def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})
@login_required
def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'confirmar_eliminacion_proveedor.html', {'proveedor': proveedor})

# Vista lista_pedidos
@login_required
def lista_pedidos(request):
    # Obtener todos los pedidos de la base de datos
    pedidos = Pedido.objects.all()

    # Crear una lista para almacenar información sobre cada pedido
    lista_pedidos_info = []

    # Iterar sobre cada pedido para obtener información relevante
    for pedido in pedidos:
        
        proveedor = pedido.insumo.proveedor.nombre
        insumo = pedido.insumo.nombre
        monto = pedido.cantidad * pedido.insumo.precio
        fecha = pedido.fecha_pedido
        estado = pedido.estado
        pedido_id = pedido.id  # Obtener el ID del pedido

        # Agregar la información del pedido a la lista
        lista_pedidos_info.append({
            'id': pedido_id,  # Agregar el ID del pedido al diccionario
            'proveedor': proveedor,
            'insumo': insumo,
            'monto': monto,
            'fecha': fecha,
            'estado': estado
        })

    # Pasar la lista de información de pedidos al contexto de la plantilla
    return render(request, 'lista_pedidos.html', {'lista_pedidos_info': lista_pedidos_info})

@login_required
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

@login_required
def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'editar_pedido.html', {'form': form})

@login_required
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'confirmar_eliminacion_pedido.html', {'pedido': pedido})
