from flask import Blueprint, request, redirect,render_template
from models.word import *


word_bp = Blueprint('word', __name__)  # для связи routers c app.py

@word_bp.route('/')
def main():
    return render_template('main.html')


@word_bp.route('/dictionary')
def dictionary():
    words = Word.query.all()
    return render_template('dictionary.html',words=words)


# @word_bp.route('/create', methods=['POST','GET'])
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         translation = request.form['translation']
#         img = request.form['img']
#         example = request.form['example']
#
#         word = Word(title=title, translation=translation, img=img,example=example)
#         db.sesion.add(word)
#         db.session.commit()
#         return redirect('/dictionary')
#     else:
#         return render_template('create.html')