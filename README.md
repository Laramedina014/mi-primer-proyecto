# Blog Django - Preentrega 10:#
- Blog web desarrollado con Django enfocado en Health Data & Bioanalytics.

Descripción:
- Este repositorio contiene la implementación del flujo CRUD completo para publicaciones y el soporte para gestión de archivos multimedia en Django. 
- Contenido: app posts, soporte de imágenes con Pillow, formularios con request.FILES, vistas para crear, listar, ver detalle, editar y eliminar posts, además de páginas estáticas (Inicio, Acerca de mí y Contacto).

Estructura del proyecto
- blog_project/: configuración principal del proyecto Django (settings.py, urls.py con configuración de media).
- osts/: aplicación con modelos (Post con ImageField), formularios (PostForm), vistas CRUD y templates.
- media/: directorio para el almacenamiento local de imágenes subidas (ignorado en Git con media/).
- manage.py: script de administración de Django.
- .gitignore: exclusión de archivos temporales (pycache), base de datos local (db.sqlite3), carpeta media/ y entorno virtual (venv/).
- requirements.txt: listado de dependencias del proyecto (Django y Pillow).

Requisitos previos:
- Python 3.10 o superior
- Git
- Instalación y puesta en marcha
- Clonar el repositorio: git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git

Entrar a la carpeta del proyecto: 
- cd TU_REPOSITORIO

Crear el entorno virtual: 
- python -m venv venv

Activar el entorno virtual:

- En Windows PowerShell: .\venv\Scripts\Activate.ps1
- Instalar dependencias: pip install -r requirements.txt

- Aplicar migraciones: python manage.py migrate

- Ejecutar el servidor de desarrollo: python manage.py runserver

- Abrir en el navegador: http://127.0.0.1:8000/

Configuración de Archivos Multimedia (Imágenes): 
- Instalación de Pillow: pip install Pillow

Configuración en settings.py:
- MEDIA_URL = '/media/' MEDIA_ROOT = BASE_DIR / 'media'

Rutas para servir imágenes en urls.py principal: 
- Se agregaron settings.MEDIA_URL y settings.MEDIA_ROOT mediante la función static() dentro del condicional if settings.DEBUG:.

Formularios HTML: 
- Se incluyó el atributo enctype="multipart/form-data" en las etiquetas <form> de creación y edición de posts para permitir la carga de imágenes (request.FILES).