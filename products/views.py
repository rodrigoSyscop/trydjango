from django.shortcuts import render

from .forms.product import ProductForm, RawProductForm
from .models import Product

def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, 'products/detail.html', context)


def product_create_view(request):
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
    else:
        form = RawProductForm()

    context = {
        "form": form
    }

    return render(request, "products/product_create.html", context)
