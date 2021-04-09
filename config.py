import os


def database_uri():
    db_user = os.environ['POSTGRES_USER']
    db_password = os.environ['POSTGRES_PASSWORD']
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']
    db_name = os.environ['POSTGRES_DB']
    database_uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    return database_uri


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
    SQLALCHEMY_DATABASE_URI = database_uri()


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
