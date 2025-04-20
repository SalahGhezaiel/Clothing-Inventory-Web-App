from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import clothing_list, clothing_create, clothing_update, clothing_delete

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('inventory/', clothing_list, name='clothing_list'),
    path('item/create/', clothing_create, name='clothing_create'),
    path('item/update/<int:pk>/', clothing_update, name='clothing_update'),
    path('item/delete/<int:pk>/', clothing_delete, name='clothing_delete'),
]