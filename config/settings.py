# mci506-andres/settings.py

# Configuration settings for the mci506-andres Data Engineering project

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///data/database.db'
    DATA_DIR = 'src/data/'
    RAW_DATA_DIR = f'{DATA_DIR}raw/'
    PROCESSED_DATA_DIR = f'{DATA_DIR}processed/'
    EXTERNAL_DATA_DIR = f'{DATA_DIR}external/'
    LOGGING_LEVEL = 'INFO'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///data/dev_database.db'
    LOGGING_LEVEL = 'DEBUG'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///data/test_database.db'
    LOGGING_LEVEL = 'ERROR'

class ProductionConfig(Config):
    DATABASE_URI = 'sqlite:///data/prod_database.db'
    LOGGING_LEVEL = 'WARNING'