# Blog Django - Preentrega 7

inicio del blog web desarrollado con Django 

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django configurado para la construcción de un blog.
Contenido: proyecto base `blog_project`, app `posts`, configuración idioma español, hoza horaria de argentina y control de versiones con Git y GitHub.

## Estructura del proyecto

- `blog_project/`: configuración principal del proyecto Django (settings, urls, wsgi).
- `posts/`: aplicación encargada de la lógica de publicaciones del blog.
- `manage.py`: script de administración de Django.
- `.gitignore`: exclusión de archivos temporales, base de datos local y entorno virtual.
- `requirements.txt`: listado de dependencias del proyecto.

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

6. Aplicar migraciones iniciales:
python manage.py migrate

7. Ejecutar el servidor de desarrollo:
python manage.py runserver

8. Abrir en el navegador:
http://127.0.0.1:8000/


