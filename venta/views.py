from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Categoria, Producto
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .serializers import ProductosSerializer, CategoriasSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index_view(request):
    request.session["usuario"]="lufernandezm"
    usuario = request.session["usuario"]
    productos = Producto.objects.all()
    context = {"usuario":usuario,"productos":productos}
    return render(request,'venta/index.html',context)

@api_view(['POST'])
def producto_add(request):
    serializer = ProductosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(["GET"])
def productos_list(request):
    productos = Producto.objects.all()
    serializer = ProductosSerializer(productos, many=True)
    return Response(serializer.data)