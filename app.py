
from flask import Flask, render_template, request, redirect
from db import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)  # создаем экземпляр приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # настройка подключения к БД
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # связываем с SQLAlchemy приложением
    migrate = Migrate(app, db)
    with app.app_context():
        from models.word import Word
        from models.user import User
        from models.userword import UserWord
        from routers.word import word_bp  # импортируем routers
        from routers.user import user_bp  # импортируем routers
        app.register_blueprint(word_bp)  # подключаем routers
        app.register_blueprint(user_bp)  # подключаем routers
        print('Создание таблиц...')
        db.create_all()  # создаем таблицы в БД
        print('таблицы созданы')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

else:
    from models.word import Word
    from models.user import User
    from models.userword import UserWord
    from db import db