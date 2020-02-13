from abc import ABC
import os

class Config(ABC):
    SECRET_KEY = os.environ["SECRET_KEY"]


class Development(Config):
    SQLALCHEMY_DATABASE_URI =  os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]


class Testing(Config):
    pass


config = {
    'development': Development,
    'testing': Testing
}