from django.urls import path

from . import views

urlpatterns = [
    # ex: /products/5/
    path('<int:id>/', views.product_detail_view, name="product_detail"),
    path('<int:id>/delete', views.product_delete_view, name="product_delete"),
    path('create/', views.product_create_view, name="product_create")
]
