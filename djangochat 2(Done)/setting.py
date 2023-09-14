# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

'''DATABASES = {
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
}'''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demo',
        'USER': 'postgres',
        'PASSWORD': 'arbisoft',
        'POST': '5434',
        'HOST': 'localhost'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
