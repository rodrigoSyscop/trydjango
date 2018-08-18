from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
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

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price'
        ]

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if len(name) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")
        return name
