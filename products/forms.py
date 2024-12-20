#Los formularios son clases

from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre")
    description = forms.CharField(max_length=200, label="Descripcion")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponible")
    photo = forms.ImageField(label="Foto", required=False)
    stock = forms.IntegerField(initial=0, label="Stock")

    def save(self):
        Product.objects.create(
            name= self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price= self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            stock=self.cleaned_data['stock'],
            photo=   self.cleaned_data['photo'],
        )
