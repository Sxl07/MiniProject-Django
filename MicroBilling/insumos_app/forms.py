from django import forms
from .models import Insumo
from .models import Proveedor
from .models import Pedido

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'descripcion', 'unidad_medida','precio' ,'proveedor']


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [ 'insumo', 'cantidad', 'estado']

        ESTADO_CHOICES =[ ('pagado', 'Pagado'),
            ('pendiente', 'Pendiente'),
            ('cancelado', 'Cancelado'), ]
            
        widgets = {
            'estado': forms.Select(choices=ESTADO_CHOICES)
        }