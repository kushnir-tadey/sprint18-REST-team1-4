from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.OrderCreate.as_view(), name="order-create"),
    path('<int:pk>/delete/', views.OrderDelete.as_view(), name='order-delete'),
    path('<int:pk>/update/', views.OrderUpdate.as_view(), name="update-order"),
    path('orders/', views.OrderListView.as_view(), name='orders'),
]