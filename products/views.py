from django.shortcuts import render, get_object_or_404, redirect

from .forms.product import ProductForm
from .models import Product


def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)

    context = {"product": product}
    return render(request, 'products/product_detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {"form": form}
    return render(request, "products/product_create.html", context)


def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect("../../")

    context = {"product": product}
    return render(request, "products/product_delete.html", context)


def product_index_view(request):
    products = Product.objects.all()
    return render(request, "products/product_index.html", {"products": products})
