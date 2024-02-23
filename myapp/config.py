class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    UPLOAD_FOLDER = "C:\\Users\\Youssef\\PycharmProjects\\BookStore\\"


class ProductionConfig(Config):
    DEBUG = False
    """postgresql://username:password@localhost:portnumber/database_name """
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:19991999@localhost:5432/flask_db"
    UPLOAD_FOLDER = "C:\\Users\\Youssef\\PycharmProjects\\BookStore\\"


AppConfig = {"dev": DevelopmentConfig, "prd": ProductionConfig}
