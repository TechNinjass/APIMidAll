from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db_instance = SQLAlchemy()

def config_sql_alchemy(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

    db_instance.app = app
    db_instance.init_app(app)

def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            db_instance.session.commit()
            return True
        except SQLAlchemyError:
            db_instance.session.rollback()
            return False
    return persist
