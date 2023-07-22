from django.urls import path

from . import views

from .views import ProductDetail

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('search_products/', views.searchProducts, name="search_products"),
    path('view_products/<slug>/', ProductDetail.as_view(), name="view_products"),
]