from django.shortcuts import render
from .models import Post

def inicio(request):
    return render(request, "posts/inicio.html")

def lista_posts(request):

    posts= Post.objects.filter(estado="publicado").order_by("-fecha_creacion")

    contexto = {
        "posts": posts,
        "page_title": "Ultimos posts"
        }


    return render (request, "posts/lista_posts.html", contexto)



def contacto(request):
    return render(request, "posts/contacto.html")

def detalle_post(request, post_id):
    post = {
        "id": post_id,
        "titulo": f"Post número {post_id}",
        "contenido": "Este es el contenido de ejemplo del post.",
        "autor": "Lara",
    }
    return render(request, "posts/detalle_posts.html", {"post": post})

def acerca(request):
    return render(request, "posts/acerca.html")