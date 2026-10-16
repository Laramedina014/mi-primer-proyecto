from blog.modelos import Autor, Blog
from blog.menu import mostrar_menu
from blog.datos import cargar_posts, guardar_posts


def main():
    # 1. Instanciamos el Blog
    mi_blog = Blog()

    # 2. Cargamos los posts desde posts.json
    mi_blog.posts = cargar_posts("posts.json")

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            # 1. Ver todos los posts
            mi_blog.listar_posts()
            

        elif opcion == 2:
            # 2. Buscar por título
            busqueda = input("\n Ingrese el título a buscar: ")
            mi_blog.buscar_por_titulo(busqueda)

        elif opcion == 3:
            # 3. Filtrar por tag
            tag = input("\n Ingrese el tag a buscar: ")
            mi_blog.filtrar_por_tag(tag)

        elif opcion == 4:
            # 4. Crear nuevo post
            print("\n--- NUEVO POST ---")
            titulo = input("Título: ")
            contenido = input("Contenido: ")
            nombre_autor = input("Nombre del autor: ")
            bio_autor = input("Bio del autor (opcional): ")
            tags_input = input("Tags separados por coma: ")

            lista_tags = [t.strip() for t in tags_input.split(",") if t.strip()]
            autor = Autor(nombre=nombre_autor, bio=bio_autor)

            nuevo = mi_blog.crear_post(
                titulo=titulo,
                contenido=contenido,
                autor=autor,
                tags=lista_tags,
                estado="Publicado",
            )
            print(f"\n ¡Post '{nuevo.titulo}' creado exitosamente! Ahora guardalo con la opcion 6")

        elif opcion == 5:
            # 5. Validar posts
            mi_blog.validar_todos_los_posts()

        elif opcion == 6:
            # 6. Guardar posts en JSON
            guardar_posts(mi_blog.posts, "posts.json")
            print("\n Posts guardados correctamente en posts.json.")

        elif opcion == 7:
            # 7. Salir (con guardado preventivo)
            guardar_posts(mi_blog.posts, "posts.json")
            print("\n ¡Gracias por usar mi blog! Hasta luego.")
            break

        else:
            print("\n Intenta de nuevo, elegí un número válido del menú.")


if __name__ == "__main__":
    main()
