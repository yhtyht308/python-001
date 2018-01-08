class BaseConfig(object):
    """config base object"""
    SECRET_KEY='makesure to set a very secret key'
    INDEX_PER_PAGE=9

class DevelopmentConfig(BaseConfig):
    """develop enviroment config"""
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class ProductionConfig(BaseConfig):
    """product enviroment config"""
    pass

class TestingConfig(BaseConfig):
    """test enviroment config"""
    pass

configs={
        'development':DevelopmentConfig,
        'production':ProductionConfig,
        'testing':TestingConfig
        }
