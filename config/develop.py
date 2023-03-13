class Config(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///clinical-history.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Test(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///clinical-history-test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024