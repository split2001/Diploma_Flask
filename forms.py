from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from models.user import User


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4,max=20)])
    email = EmailField('Email', validators=[DataRequired(), Length(min=4,max=20)])
    password = PasswordField('Пароль',validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль',validators=[DataRequired(),
                                                                      EqualTo('password', message='Пароли не совпадают.')])
    submit = SubmitField('Зарегистрироваться')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Пользователь уже существует.')


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')