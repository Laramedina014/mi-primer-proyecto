class Autor:
    def __init__(self, nombre, bio="", especialidad="", redes_sociales= None):
        self.nombre= nombre
        self.bio= bio
        self.especialidad= especialidad
        self.redes_sociales= redes_sociales if redes_sociales is not None else []

    def to_dicc(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales

        }
        
class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id=id
        self.titulo=titulo
        self.contenido=contenido
        self.autor= autor
        self.tags= tags
        self.estado= estado

    def to_dicc(self):
        
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dicc(),
            "estado": self.estado,
        }

class Blog:
    def __init__(self):
        self.posts=[]

    def obtener_posts(self):
        return self.posts

    def crear_post(self, titulo, contenido, autor, tags, estado):
        nuevo_id= len(self.posts) + 1
        nuevo_post= Post(
            id= nuevo_id,
            titulo=titulo,
            contenido=contenido,
            autor=autor,
            tags=tags,
            estado=estado,
        )
        self.posts.append(nuevo_post)
        return nuevo_post

    def listar_posts(self):
        

        if not self.posts:
            print("\n No hay posts disponibles para mostrar. Porfavor, carga los post.")
            return

        print("\n --- TODOS LOS POST DISPONIBLES --- ")
        for post in self.posts:
            print(f"- [{post.id}] {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")


    def buscar_por_titulo(self, busqueda_titulo):
        busqueda = busqueda_titulo.lower().strip()
        encontrados = []

        if busqueda == "":
            print("\n El titulo a buscar no puede estar vacio.")    
            return []

        for post in self.posts:
            if busqueda in post.titulo.lower():
                encontrados.append(post)

        if encontrados:
            print(f"\n Resultados encontrados para '{busqueda}': ")
            for post in encontrados:
                print(f"- [{post.id}] {post.titulo} | Autor: {post.autor.nombre}")
        else: 
            print("\n No se encontraron resultados para ese titulo.")
        return encontrados

    def filtrar_por_tag(self, busqueda_tag):
        busqueda= busqueda_tag.lower().strip()
        encontrados = []

        for post in self.posts:
            if isinstance(post.tags, list):
                for tag in post.tags:
                    if str(tag).lower().strip() == busqueda:
                        encontrados.append(post)
                        break

        if busqueda == "":
            print("\n El tag a buscar no puede estar vacio.")
            return []
        elif encontrados:
            print(f"\n Posts con el tag '{busqueda}':")
            for post in encontrados:
                print(f"- [{post.id}] {post.titulo} | Autor: {post.autor.nombre}")
        else:
            print(f"\n No se encontraron posts con ese tag.")
        return encontrados

    def validar_post(self, post):
        errores = []

        if post.titulo.strip() == "":
            errores.append("\n El título no puede estar vacío.")

        if post.contenido.strip() == "":
            errores.append("\n El contenido no puede estar vacío.")

        if len(post.tags) == 0:
            errores.append("\n El post debe tener al menos una etiqueta.")

        if post.estado not in ("Borrador", "Publicado", "Archivado"):
            errores.append("\n El estado del post no es válido.")
            
        return errores


    def validar_todos_los_posts(self):
        print("\n--- VALIDACIÓN DE POSTS ---")

        if not self.posts:
            print("\n No hay posts para validar")
            return

        for post in self.posts:
            errores = self.validar_post(post)

            if not errores:
                print(f"\n [CORRECTO] Post {post.id}: '{post.titulo}' es valido.")

            else:
                errores_str = ", ".join(errores)
                print(f"\n [INCORRECTO] Post {post.id}: {errores_str}")
