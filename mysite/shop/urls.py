from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('shoes/', views.ShopView.as_view(), name='shop-shoes'),
    path('shoes/detail/<int:pk>/', views.ShopItemDetail.as_view(), name='shoes_detail'),
    path('additem/<int:pk>/', views.AddItem.as_view(), name='add_item'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout')
]
