from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "placeholder": "Product name..."
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs = {
                "placeholder": "Product description...",
                "class": "some-css-class",
                "rows": "5",
                "cols": "50"
            }
        )
    )
    price       = forms.DecimalField()
