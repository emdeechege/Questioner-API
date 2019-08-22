import os


class Config():
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET')
    DATABASE_URL = os.getenv('DATABASE_URL')



class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    ENV = "development"
    DATABASE_URL = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    ENV = os.getenv('TEST_ENV')
    DATABASE_URL = os.getenv('DATABASE_TEST_URL')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': Config,
}
