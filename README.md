# Blog por Consola - Preentrega 6 (POO y Persistencia JSON)

Este proyecto contiene **Programación Orientada a Objetos (POO)** y **persistencia de datos mediante JSON**, en el marco de la Diplomatura en Data Science.

---

## 📁 Estructura del proyecto

```text
blog_consola/            # carpeta raiz
│
├── main.py              # Bloque de codigo principal
├── README.md            # Documentación del proyecto
├── posts.json           # Archivo de persistencia de datos en formato JSON
│
└── blog/                # Paquete con los módulos de lógica
    ├── __init__.py      # Inicializador del paquete blog
    ├── modelos.py       # Definición de clases: Autor, Post y Blog (POO)
    ├── datos.py         # Carga, guardado y serialización de objetos hacia/desde JSON
    ├── menu.py          # Interfaz de usuario por consola y presentación del menú
    ├── operaciones.py   # Funciones auxiliares de búsqueda y filtrado
    └── validaciones.py  # Reglas de validación para los posts
