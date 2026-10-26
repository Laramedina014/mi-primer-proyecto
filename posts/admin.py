# Register your models here.
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    #define qué columnas queremos ver en la tabla principal del admin
    list_display = ("titulo", "autor", "fecha_creacion", "estado")

    #agrega una barra de búsqueda.
    search_fields = ("titulo", "contenido", "autor")

    #agrega filtros laterales.
    list_filter = ("estado", "fecha_creacion")

    #permite editar ese campo desde la lista.
    list_editable= ("estado", )

admin.site.register(Post, PostAdmin)

admin.site.site_header = "Administración de Mi Blog"
admin.site.site_title = "Panel del Blog"
admin.site.index_title = "Gestión de contenidos"

"""Con esto, el panel de administración permite:

Ver los posts en una tabla clara.
Buscar por título, contenido o autor.
Filtrar por estado de publicación.
Filtrar por fecha de creación.
Cambiar rápidamente si un post está publicado."""