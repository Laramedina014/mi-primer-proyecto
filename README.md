# Blog Django - Preentrega 10

Blog web desarrollado con Django enfocado en Health Data & Bioanalytics.

## Descripción

Este repositorio contiene la implementación del flujo CRUD completo para publicaciones y el soporte para gestión de archivos multimedia en Django.
Contenido: app `posts`, soporte de imágenes con `Pillow`, formularios con `request.FILES`, vistas para crear, listar, ver detalle, editar y eliminar posts, además de páginas estáticas (Inicio, Acerca de mí y Contacto).

## Estructura del proyecto

- `blog_project/`: configuración principal del proyecto Django (`settings.py`, `urls.py` con configuración de `media`).
- `posts/`: aplicación con modelos (`Post` con `ImageField`), formularios (`PostForm`), vistas CRUD y templates.
- `media/`: directorio para el almacenamiento local de imágenes subidas (ignorado en Git).
- `manage.py`: script de administración de Django.
- `.gitignore`: exclusión de archivos temporales (`__pycache__`), base de datos local (`db.sqlite3`) y entorno virtual (`venv/`).
- `requirements.txt`: listado de dependencias del proyecto (incluye `Django` y `Pillow`).

## Requisitos previos

- Python 3.10 o superior
- Git

## Instalación y puesta en marcha

1. Clonar el repositorio:
git clone URL_DE_TU_REPOSITORIO_EN_GITHUB

2. Entrar a la carpeta del proyecto:
cd blog_consola

3. Crear el entorno virtual:
python -m venv venv

4. Activar el entorno virtual:
- En Windows PowerShell:
.\venv\Scripts\Activate.ps1

5. Instalar dependencias:
pip install -r requirements.txt

6. Aplicar migraciones:
python manage.py migrate

7. Ejecutar el servidor de desarrollo:
python manage.py runserver

8. Abrir en el navegador:
http://127.0.0.1:8000/
