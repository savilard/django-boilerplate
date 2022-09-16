from config.settings.environs import env

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG', cast=bool, default=False)
