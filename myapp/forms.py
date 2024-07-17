from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'imagen', 'descripcion', 'precio', 'important']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        } 
 