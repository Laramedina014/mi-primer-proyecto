def crear_separador():
    return "-" * 40

def formatear_post(post):
    titulo= post["titulo"]
    estado= post["estado"]
    autor= post["autor"]["nombre"]
    tags= ", ".join(post["tags"])

    return f"""
Titulo: {titulo}
Autor: {autor}
Estado: {estado}
Etiquetas: {tags}
"""

def listar_posts(lista_posts):
    for post in lista_posts:
        print(crear_separador())
        print(formatear_post(post))