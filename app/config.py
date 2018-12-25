
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'tHjM/}9*}Q:;Kz#p@\\ZA^w\"=S*xkg|]FxL{=q'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOKEN_VALIDITY = 15    # seconds
