
from flask import Blueprint, request, redirect, render_template, flash, url_for
from werkzeug.utils import secure_filename
from models.word import Word
from extensions import db
import os

word_bp = Blueprint('word', __name__)  # для связи роутеров с app.py

UPLOAD_FOLDER = 'static/uploads'


@word_bp.route('/')
def main():
    return render_template('main.html')


@word_bp.route('/dictionary',methods=['POST', 'GET'])
def dictionary():
    if request.method == 'POST':
        search_word = request.form['search']
        words = Word.query.filter(Word.title.ilike(f'{search_word}')).all() or Word.query.filter(Word.translation.ilike(f'{search_word}')).all()   # используем
        # ilike для нечувствительнсти к регистру при поиске
    else:
        words = Word.query.all()
    return render_template('dictionary.html', words=words)


@word_bp.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        translation = request.form['translation']
        description = request.form['description']
        img = request.files['img']

        # Проверка на существование слова
        existing_word = Word.query.filter_by(title=title).first()
        if existing_word:
            error = 'Такое слово уже существует'
            return render_template('create.html', error=error)

        # Сохранение изображения, если оно есть
        filename = None
        if img and img.filename:
            filename = secure_filename(img.filename)
            img_path = os.path.join(UPLOAD_FOLDER, filename)
            img.save(img_path)

        # Создание нового объекта слова
        word = Word(title=title, translation=translation, description=description, img=filename)
        db.session.add(word)
        db.session.commit()
        return redirect('/dictionary', )
    else:
        return render_template('create.html')