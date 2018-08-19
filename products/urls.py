from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path('', views.product_index_view, name="product_index"),
    # ex: /products/5/
    path('<int:id>/', views.product_detail_view, name="product_detail"),
    path('<int:id>/delete/', views.product_delete_view, name="product_delete"),
    path('create/', views.product_create_view, name="product_create")
]
