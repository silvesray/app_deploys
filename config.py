import os
from os.path import join, dirname, abspath, isdir


class Config:
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG","JPG", "PNG", "GIF"]
    IMAGE_UPLOADS = join(abspath(dirname(__file__)), "app","static","img", "uploads")\
        if isdir("/app/static/img/uploads") else join("/app","static","img", "uploads")
    MAX_CONTENT_LENGTH = 1.0 * 1024 * 1024
    MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024
    CLIENT_IMAGES = join(abspath(dirname(__file__)), "app","static", "img", "downloads")\
        if isdir("/app/static/img/downloads") else join("/app", "static", "img", "downloads")
    CLIENT_REPORT = None
    UPLOAD_DIRECTORY = join(abspath(dirname(__file__)), "app","static", "img", "uploads")\
        if isdir("/app/static/img/uploads") else join("/app", "static", "img", "uploads")
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass
