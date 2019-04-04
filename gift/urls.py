from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('addresses/', views.AddressesList.as_view(), name='addresses_list'),
    path('addresses/<int:pk>', views.AddressesDetail.as_view(),
         name='addresses_detail'),
    path('boxes/', views.BoxesList.as_view(), name='boxes_list'),
    path('boxes/<int:pk>', views.BoxesDetail.as_view(), name='boxes_detail'),
    path('items/', views.ItemsList.as_view(), name='items_list'),
    path('items/<int:pk>', views.ItemsDetail.as_view(), name='items_detail'),
    path('users/', views.UsersList.as_view(), name='users_list'),
    path('users/<int:pk>', views.UsersDetail.as_view(), name='users_detail'),
    path('orders/', views.OrdersList.as_view(), name='orders_list'),
    path('orders/<int:pk>', views.OrdersDetail.as_view(), name='orders_detail'),
]
