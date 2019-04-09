DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vpm_db',
        'USER': '',
        'PASSWORD': '',
        'TEST': {
            'NAME': 'testdb',
        },
	'PORT': 5433,
    }
}

DEBUG = True

EMAIL_HOST = '127.0.0.1'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 1025
EMAIL_USE_TLS = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

WEBAPP_BASE_URL = 'http://localhost:8001/#!/'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_REGEX_WHITELIST = (
    'localhost:8001',
)

CORS_ALLOW_HEADERS = ['*']

ALLOWED_HOSTS = ['*']

CELERY_BROKER_URL = 'amqp://oforvjam:opWRlZSVIuYVlcC5dFMwlo_hQu3t55ic@elephant.rmq.cloudamqp.com/oforvjam'
