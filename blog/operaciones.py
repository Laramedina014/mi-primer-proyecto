# 3. Función para listar posts
def listar_posts(lista):
    print("\n--- TODOS LOS POSTS DISPONIBLES ---")
    
    for post in lista:
        print(f"- {post["titulo"]} | Autor: {post["autor"]["nombre"]}")
        
# 4. Funciones de búsqueda y filtrado
def buscar_por_titulo(lista_posts, busqueda_titulo):
    busqueda = busqueda_titulo.lower()
    encontrados = []

    for post in lista_posts:
        titulo = post["titulo"].lower()

        if busqueda in titulo:
            encontrados.append(post)
        
    if busqueda == "":
        print("El titulo a buscar no puede estar vacio.")    
    elif encontrados:
        print(f"Resultados encontrados para '{busqueda}':")
        listar_posts(encontrados)
    else:
        print(f"No se encontraron resultados para ese titulo.")


def filtrar_por_tag(lista_posts, busqueda_tag):
    busqueda= busqueda_tag.lower()
    encontrados = []

    for post in lista_posts:
        tags = post["tags"]
        if type(tags) == list:
            for tag in tags:
                if (tag).lower() == busqueda_tag:
                    encontrados.append(post)
                    break

    if busqueda == "":
        print("El tag a buscar no puede estar vacio.")
    elif encontrados:
        print(f"Posts con el tag '{busqueda}':")
        listar_posts(encontrados)
    else:
        print(f"No se encontraron posts con ese tag.")


