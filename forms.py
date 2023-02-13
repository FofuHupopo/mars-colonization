from flask_wtf import form
from wtforms import fields, validators


class SurveyForm(form.FlaskForm):
    surname = fields.StringField("Фамилия", validators=[validators.DataRequired(), validators.length(1, 100)])
    name = fields.StringField("Имя", validators=[validators.DataRequired(), validators.length(1, 100)])
    education = fields.StringField("Образование", validators=[validators.DataRequired(), validators.length(1, 100)])
    profession = fields.StringField("Профессия", validators=[validators.DataRequired(), validators.length(1, 100)])
    sex = fields.SelectField("Пол", choices=[
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    ])
    motivation = fields.StringField("Мотивация", validators=[validators.DataRequired(), validators.length(1, 512)])
    is_ready = fields.BooleanField(
        "Готовы остаться на марсе?",
    )
    submit = fields.SubmitField("Ответить")