from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', SnackList.as_view(),name='snacks_list'),
    path('create/', SnackCreate.as_view(),name='snack_create'),
    path('<pk>/delete', SnackDelete.as_view(),name='snack_delete'),
    path('<pk>/', SnackDetail.as_view(),name='snack_detail'),
    path('<pk>/update', SnackUpdate.as_view(),name='snack_update'),
    
]
