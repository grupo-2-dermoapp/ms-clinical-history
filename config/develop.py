class Config(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///clinical-history.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False