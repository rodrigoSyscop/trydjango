from django.shortcuts import render

from .models import Product

def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, 'products/detail.html', context)
