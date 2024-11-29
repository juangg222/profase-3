import os
from pathlib import Path

# BASE_DIR es la ruta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad: Cambia la clave secreta en producción
SECRET_KEY = 'tu-clave-secreta-aqui'

# Activar modo debug solo en desarrollo
DEBUG = True

ALLOWED_HOSTS = []  # Agrega tus dominios o direcciones IP aquí

# Aplicaciones instaladas
INSTALLED_APPS = [
    'colorfield',
    'admin_interface',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'barberia_app',  # Tu aplicación
]

# Configuración adicional
X_FRAME_OPTIONS = 'SAMEORIGIN'  # Necesario para que funcione admin-interface

 

# Middleware que maneja varias funciones, como la seguridad y las sesiones
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de las rutas de la URL
ROOT_URLCONF = 'barberia.urls'

# WSGI aplicación para la implementación del servidor
WSGI_APPLICATION = 'barberia.wsgi.application'

# Configuración de la base de datos (usa MySQL en lugar de SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Usamos el backend de MySQL
        'NAME': 'kapper',  # Cambia esto al nombre de tu base de datos
        'USER': 'root',            # Cambia esto por tu usuario de MySQL
        'PASSWORD': '6232',     # Cambia esto por tu contraseña de MySQL
        'HOST': 'localhost',                   # Si estás trabajando en tu máquina local
        'PORT': '3306',                        # El puerto por defecto de MySQL
    }
}

# Configuración de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de archivos estáticos (CSS, JS, imágenes, etc.)
STATIC_URL = 'static/'

# Configuración de archivos multimedia (imágenes subidas por el usuario, etc.)
MEDIA_URL = 'media/'

# Configuración de la plantilla (si la usas en tu proyecto)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Ruta de los archivos estáticos adicionales
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Zona horaria y configuración regional
LANGUAGE_CODE = 'es-ES'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configuración para sesiones
SESSION_COOKIE_AGE = 3600  # 1 hora de duración de sesión
