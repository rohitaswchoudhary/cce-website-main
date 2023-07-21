import os
from pickle import FALSE
import shutil
from pathlib import Path
from dotenv import load_dotenv
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()
# SECRET_KEY = os.environ["SECRET_KEY"]
SECRET_KEY = "tgsdfhyagfgahvgugsfhyhzycuyghuihufuyhfd5841584858zsbcbjhhvbifvuh"

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'departments',
    'aboutCCE',
    'administration',
    'studentservices',
    'placements',
    'storages',
    'tailwind',
    'cce_web_theme'

]


MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]


# Development Settings

if os.getenv('PRODUCTION') != 'True':
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")
    INSTALLED_APPS.append("django_browser_reload")
    DEBUG = True


ROOT_URLCONF = 'cce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
        
    },
]

WSGI_APPLICATION = 'cce.wsgi.application'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USERNAME'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT')
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Added by manually
# custom settings
if os.getenv('PRODUCTION') != 'True':
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
INTERNAL_IPS = [
    "127.0.0.1",
]


# AWS_S3_URL_PROTOCOL='http:'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'www.assets.cce.edu.in'
AWS_S3_CUSTOM_DOMAIN =  "dnbca6q7do6n.cloudfront.net"
# PUBLIC_MEDIA_LOCATION = 'media'
# MEDIA_URL = 'http://' + AWS_S3_CUSTOM_DOMAIN + '/' + PUBLIC_MEDIA_LOCATION + '/'
# DEFAULT_FILE_STORAGE = 'cce.storage_backends.MediaStorage'

MEDIA_URL = '/media/'




TAILWIND_APP_NAME = 'cec_ee_web_theme'
# Jazzmin settings


JAZZMIN_UI_TWEAKS = {
    "theme": "cerulean",
    "dark_mode_theme": "cerulean",
}


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "CEC_EE Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "EE",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "EE",

    # # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "favicons/EE.png",
    "site_logo_small": "favicons/EE.png",

    "site_favicon": "favicons/EE.png",
     "login_logo": "favicons/android-chrome-192x192.png",


    # # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    # "site_icon": None,

    # # Welcome text on the login screen
    "welcome_sign": "Welcome Administration Page of CEC_EE ",

    # # Copyright on the footer
    "copyright": " Electrical Engineering Department CEC",



    # # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index",
            "permissions": ["auth.view_user"]},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"Main Website": "website"},
        {"Departments": "departments"},
    ],

    "related_modal_active": True,
}


