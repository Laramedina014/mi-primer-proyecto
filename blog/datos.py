import json
from blog.modelos import Autor, Post

# 1. Definición de datos iniciales
perfil_autor = {
    "nombre": "Lara Medina",
    "bio": "Estudiante de Data Science enfocada en analítica aplicada a la salud y HealthTech",
    "especialidad": "Health Data & Bioanalytics",
    "redes_sociales": ["github.com/laramedina", "linkedin.com/in/laramedina"]
}

estados_post = ("Borrador", "Publicado", "Archivado")
etiquetas_blog = {"HealthTech", "Pandas", "Hospitales", "EDA", "Machine Learning", "Tiempos de Espera"}

posts = [
    {
        "id": 1,
        "titulo": "Analisis de tiempos de espera en guardias hospitalarias con Python y Pandas",
        "contenido": "Exploracion de tiempos de triage y optimizacion de turnos medicos con Pandas.",
        "autor": perfil_autor,
        "tags": ["HealthTech", "Pandas", "Hospitales"],
        "estado": estados_post[1]  # Publicado
    },
    {
        "id": 2,
        "titulo": "Limpieza y anonimizacion de registros clinicos segun normativas de privacidad",
        "contenido": "Tecnicas de enmascaramiento de datos personales en historias clinicas con Python.",
        "autor": perfil_autor,
        "tags": ["HealthTech", "Data Privacy", "Data Cleaning"],
        "estado": estados_post[1]  # Publicado
    },
    {
        "id": 3,
        "titulo": "Modelo predictivo para reingresos de pacientes cronicos en 30 dias",
        "contenido": "Prototipo de clasificacion para identificar riesgo de rehospitalizacion temprana.",
        "autor": perfil_autor,
        "tags": ["Machine Learning", "HealthTech", "EDA"],
        "estado": estados_post[0]  # Borrador
    },
    {
        # Post con errores a propósito para probar las validaciones
        "id": 4,
        "titulo": "",  # Título vacío
        "contenido": "Faltan tags válidos y el estado no existe en la tupla.",
        "autor": perfil_autor,
        "tags": "no-es-una-lista",  # Tipo incorrecto
        "estado": "Invalido"  # No está en estados_post
    }
]



def crear_post_desde_dicc(datos):
    datos_autor = datos.get("autor", {})
    autor_objeto = crear_autor_desde_dicc(datos_autor)

    
    post = Post(
        id=datos.get("id", 1),
        titulo=datos.get("titulo", ""),
        contenido=datos.get("contenido", ""),  
        autor=autor_objeto,
        tags=datos.get("tags", []),
        estado=datos.get("estado", "Publicado")
    )
    return post

def crear_autor_desde_dicc(datos_autor):
    return Autor(
        nombre=datos_autor.get("nombre", "Sin nombre"),
        bio=datos_autor.get("bio", ""),
        especialidad=datos_autor.get("especialidad", ""),
        redes_sociales=datos_autor.get("redes_sociales", [])
    )



def guardar_posts(posts, ruta="posts.json"):
    posts_to_dicc=[]

    for post in posts:
        posts_to_dicc.append(post.to_dicc())

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(posts_to_dicc, archivo, indent=4, ensure_ascii=False)


def cargar_posts(ruta="posts.json"):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos= json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

    posts=[]
    for item in datos:
        post= crear_post_desde_dicc(item)
        posts.append(post)
    return posts