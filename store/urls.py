from django.urls import path

from . import views

# giving url paths to the views
# Leave as empty string for base url
urlpatterns = [
   path('', views.store, name="store"),
   path('cart/', views.cart, name="cart"),
   path('checkout/', views.checkout, name="checkout"),

]