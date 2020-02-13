"""
Django settings for django_07 project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&i3l5)rk+on#popjpca98g1@z7e%pz=6691&55#^-#c7%b-31!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App01.apps.App01Config',
    'captcha', # 安装第三方应用
    'App02',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_07.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'django_07.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'day07',
        # 'NAME': 'bbs',
        'HOME': 'local',
        'USER': 'root',
        'PASSWORD': '123456.',
        'PORT': 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'



# django_simple_captcha 验证码配置
# https://django-simple-captcha.readthedocs.io/en/latest/advanced.html
# 格式
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s'
# 噪点样式
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_null', # 没有样式
    'captcha.helpers.noise_arcs', # 线
    'captcha.helpers.noise_dots', # 点
)
# 图片大小
CAPTCHA_IMAGE_SIZE = (100, 25)
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' # 图片中的文字为随机英文字母，如 mdsh
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'    # 图片中的文字为数字表达式，如1+2=</span>
CAPTCHA_LENGTH = 4 # 字符个数
CAPTCHA_TIMEOUT = 1 # 超时(minutes)


# 分页
COUNT_OF_PAGE = 10   # 每页10条记录