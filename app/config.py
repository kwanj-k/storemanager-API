"""Configuration file for the API """

class Config(object):
    """Parent configuration class"""
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Configuration"""
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Configuration"""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
