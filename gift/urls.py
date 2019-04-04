from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('addresses/', views.AddressList.as_view(), name='address_list'),
    path('addresses/<int:pk>', views.AddressDetail.as_view(), name='address_detail'),
]