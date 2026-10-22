from django.shortcuts import render

def inicio(request):
    return render(request, "posts/inicio.html")

def lista_posts(request):
    posts = [
        {"id": 1,
         "titulo": "Analisis de tiempos de espera en guardias hospitalarias con Python y Pandas",
         "contenido": "Exploracion de tiempos de triage y optimizacion de turnos medicos con Pandas.",
         "autor": "Lara"},

        {"id": 2,
         "titulo": "Limpieza y anonimizacion de registros clinicos segun normativas de privacidad",
         "contenido":"Tecnicas de enmascaramiento de datos personales en historias clinicas con Python.",
         "autor": "Lara"},

        {"id": 3,
         "titulo": "Modelo predictivo para reingresos de pacientes cronicos en 30 dias",
         "contenido": "Prototipo de clasificacion para identificar riesgo de rehospitalizacion temprana.", 
         "autor": "Lara"},
    ]
    contexto = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", contexto)

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