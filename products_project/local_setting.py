# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cf_1&91m@%_^bh*g3uu!4*i4qi8tk$%2be5rlf(#p&81lvc3*x'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password'
    }
}
