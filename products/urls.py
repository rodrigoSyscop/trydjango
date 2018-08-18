from django.urls import path

from . import views

urlpatterns = [
    # ex: /products/5/
    path('<int:product_id>/', views.product_detail_view, name='products_detail')
]
