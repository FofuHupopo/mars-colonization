from flask import request, redirect, render_template, url_for
from flask.views import View


class IndexView(View):
    def dispatch_request(self, title: str):
        context = {
            "title": title
        }
        return render_template("index.html", **context)


class TrainingView(View):
    PROF_TO_TARINING_MAP = {
        "engineer": {
            "image_url": "images/spaceship/spaceship-plan--engineer-mark.png",
            "subtitle": "Инженерные тренажеры"
        },
        "scientist": {
            "image_url": "images/spaceship/spaceship-plan--scientist-mark.png",
            "subtitle": "Научные симуляторы"
        }
    }
    PROF_NAME_TO_PROF_TYPE = {
        "инженер": "engineer",
        "строитель": "engineer",
        "ученый": "scientist",
        "врач": "scientist"
    }

    def dispatch_request(self, prof: str):
        context = {
            "image_url": "",
            "subtitle": "Отдыхайте. Для вас пока что нет работы..."
        }
        
        prof_type = TrainingView.PROF_NAME_TO_PROF_TYPE.get(prof)
        
        if prof_type:
            context = TrainingView.PROF_TO_TARINING_MAP[prof_type]

        return render_template("prof.html", **context)