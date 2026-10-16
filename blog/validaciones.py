def validar_post(post):
    errores = []
    if post["titulo"] == "":
        errores.append("El título no puede estar vacío.")

    if post["contenido"] == "":
        errores.append("El contenido no puede estar vacío.")

    if len(post["tags"]) == 0:
        errores.append("El post debe tener al menos una etiqueta.")

    if post["estado"] not in ("Borrador", "Publicado", "Archivado"):
        errores.append("El estado del post no es válido.")
        
    return errores


def validar_todos_los_posts(lista_posts):
    print("\n--- VALIDACIÓN DE POSTS ---")

    for post in lista_posts:
        errores = validar_post(post)

        if not errores:
            print(f"[CORRECTO] Post {post['id']}: '{post['titulo']}' es valido.")

        else:
            errores_str = ", ".join(errores)
            print(f"[INCORRECTO] Post {post['id']}: {errores_str}")