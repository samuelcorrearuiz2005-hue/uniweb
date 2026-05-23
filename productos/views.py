from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Producto
    
# Registro de productos(CREATE)
def registrar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")

        Producto.objects.create(nombre=nombre, precio=precio)

        return redirect("lista_productos")

    return render(request, "productos/registro_producto.html")

# Lista de producto(READ)
def lista_productos(request):

    productos = Producto.objects.all()
    
    for producto in productos:
        producto.precio_formato = f"{int(producto.precio):,}".replace(",", ".") + " COP"

    return render(request, "productos/lista_productos.html", {"productos": productos})

# Editar producto(UPDATE)
def editar_productos(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        producto.nombre = request.POST.get("nombre")
        producto.precio = request.POST.get("precio")
        producto.save()
        return redirect("lista_productos")

    return render(request, "productos/editar_productos.html", {
        "producto": producto
    })

# Eliminar productos(DELETE)
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    
    return redirect("lista_productos")