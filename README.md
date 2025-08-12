# 🚀 Django Portafolio y Blog

Este proyecto es un portafolio personal con sección de blog, construido con Django.
Contiene dos módulos principales:

- 📁 **portfolio**: muestra proyectos personales
- 📰 **blog**: muestra publicaciones (posts)

***

## 🛠️ Requisitos Previos

Antes de empezar, asegúrate de tener instalado lo siguiente:

- 🐍 Python 3.8+
- 📦 pip (gestor de paquetes de Python)
- 🧪 Virtualenv (opcional pero recomendado)
- 💾 SQLite (incluido con Python para la base de datos)

***

## ⚙️ Instalación y configuración

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd portfolio
```

2. **Crear y activar entorno virtual**

Linux / macOS:

```bash
python3 -m venv venv_portafolio
source venv_portafolio/bin/activate
```

Windows:

```cmd
python -m venv venv_portafolio
venv_portafolio\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

> 📌 Asegúrate que `requirements.txt` contenga al menos `Django==5.2.5` y otras librerías necesarias.

4. **Aplicar migraciones a la base de datos**
```bash
python manage.py migrate
```

5. **(Opcional) Crear usuario administrador**
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**

- 🏠 Portafolio: `http://127.0.0.1:8000/`
- 📰 Blog: `http://127.0.0.1:8000/blog/`
- 🔧 Admin: `http://127.0.0.1:8000/admin/`

***

## 📁 Archivos importantes

- `manage.py` — script para gestionar el proyecto Django
- `portfolio/` — aplicación del portafolio
- `blog/` — aplicación del blog
- `dj_settings/settings.py` — configuración principal del proyecto
- `db.sqlite3` — base de datos SQLite por defecto
- `media/` — carpeta para archivos subidos (imágenes, etc)
- `static/` — archivos estáticos compilados para producción

***

## 🚦 Consideraciones para producción

- 🔒 Cambiar `DEBUG` a `False` en `dj_settings/settings.py`
- 🌐 Configurar `ALLOWED_HOSTS` con tu dominio o IP
- 📦 Ejecutar `python manage.py collectstatic` para copiar archivos estáticos a `STATIC_ROOT`
- 🚀 Configurar servidor WSGI/ASGI (ejemplo: Gunicorn, uWSGI)
- 🗂️ Servir archivos estáticos y media a través del servidor web (ej. Nginx)
- 🛢️ Configurar base de datos adecuada para producción (PostgreSQL, MySQL, etc.)

***

## 📦 Uso de media y archivos estáticos

- 🖼️ Archivos de usuario (imágenes de proyectos, posts) se almacenan en `media/`
- 🎨 Archivos estáticos como CSS, JS, imágenes del portafolio están en `portfolio/static/` y luego se colectan a `staticfiles/` para producción.

***

## 🌐 Rutas principales y URLs

- `/` : Página principal del portafolio
- `/blog/` : Página listando posts del blog
- `/blog/<id>` : Detalle de un post
- `/admin/` : Panel administrador Django

***

## 📋 Dependencias recomendadas

- Django 5.2.x
- Bootstrap 5 (frontend, ya incluido en archivos estáticos)
- Pillow (para gestionar imágenes en Django)

***

## 🚀 Ejemplo rápido para agregar un proyecto

1. Accede a admin: `http://127.0.0.1:8000/admin/`
2. Selecciona `Projects` y crea nuevo proyecto con título, descripción, imagen, URL y fecha.

***

## 🛠️ Ayuda y soporte

Si surge alguna duda o error, revisa:

- 📝 Consola de ejecuciones y errores
- 📂 Archivos de log (si están configurados)
- 📚 Documentación oficial de Django

***

¡🎉 Feliz desarrollo!


