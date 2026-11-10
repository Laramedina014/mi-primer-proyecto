from django.urls import path
from . import views

urlpatterns = [
    # Páginas generales
    path("", views.inicio, name="inicio"),
    path("acerca/", views.acerca, name="acerca"),
    path("contacto/", views.contacto, name="contacto"),

    # Rutas de Posts
    path("posts/", views.lista_posts, name="lista_posts"),
    path("posts/crear/", views.crear_post, name="crear_post"),
    path("posts/<slug:slug>/", views.detalle_post, name="detalle_post"),
    path("posts/<slug:slug>/editar/", views.editar_post, name="editar_post"),
    path("posts/<slug:slug>/eliminar/", views.eliminar_post, name="eliminar_post"),
]


