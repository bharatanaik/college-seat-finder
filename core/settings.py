from pathlib import Path
from django.core.management.commands.runserver import Command as runserver
runserver.default_port = "8050"

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '6sv^9hz4tyvu#9rf344*)a9#te_qd@v#6c3j#og)up(x6f$@v*'

# Change DEBUG to False before uploading to github
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'main','admissions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps'
]


"""PRODUCTION SETTINGS (DEBUG = FALSE)"""
if not DEBUG:
    ALLOWED_HOSTS = ['collegeseatfinder.com', 'www.collegeseatfinder.com']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 518400 
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "iapshoyw_collegeseatfinder",
        "USER": "iapshoyw_user",
        "PASSWORD": r"WK0meaH%F3@i",
        "HOST": "npuspta.org",
        "PORT": 3306,
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}


# DATABASES = {
#     "default":{
#         "ENGINE":"django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3"
#     }
# }

LOGOUT_REDIRECT_URL = "index"

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_ROOT = "static_files"
