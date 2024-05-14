from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_view,name=''),
    path('index/',views.index_view,name='index'),

    path('productos_list',views.productos_list, name='productos_list'),
    path('producto_add/',views.producto_add, name='producto_add'),
]
