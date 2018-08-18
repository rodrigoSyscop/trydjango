from django.shortcuts import render

from .forms.product import ProductForm
from .models import Product

def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, 'products/detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }

    return render(request, "products/product_create.html", context)
