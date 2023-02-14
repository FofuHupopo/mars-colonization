from flask import request, redirect, render_template, url_for
from flask.views import View, ft

import forms


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

    def dispatch_request(self, prof: str) -> ft.ResponseReturnValue:
        context = {
            "image_url": "",
            "subtitle": "Отдыхайте. Для вас пока что нет работы..."
        }
        
        prof_type = TrainingView.PROF_NAME_TO_PROF_TYPE.get(prof)
        
        if prof_type:
            context = TrainingView.PROF_TO_TARINING_MAP[prof_type]

        return render_template(
            "prof/prof.html",
            **context
        )
    

class ProfListView(View):
    PROF_LIST = (
        "инженер-исследователь", "пилот", "строитель", "экзобиолог",
        "врач", "инженер по терраформированию", "климатолог",
        "специалист по радиационной защите", "астрогеолог",
        "гляциолог", "инженер жизнеобеспечения", "метеоролог",
        "оператор марсохода", "киберинженер", "штурман", "пилот дронов",
    )
    
    def dispatch_request(self, list: str=None) -> ft.ResponseReturnValue:
        context = {
            "prof_list": ProfListView.PROF_LIST,
            "list_type": list
        }

        return render_template(
            "prof/prof-list.html",
            **context
        )


class SurveyView(View):
    methods = ["get", "post"]

    def dispatch_request(self) -> ft.ResponseReturnValue:
        survey_form = forms.SurveyForm()
        
        if survey_form.validate_on_submit():
            return render_template('survey/auto_answer.html', form=survey_form)
        
        return render_template('survey/survey.html', form=survey_form)


class EmergencyAccessView(View):
    methods = ["get", "post"]

    def dispatch_request(self) -> ft.ResponseReturnValue:
        access_form = forms.EmergancyAccessForm()
        
        if access_form.validate_on_submit():
            return redirect("/index/Главная")
        
        return render_template('emergency-access.html', form=access_form)


class DistributionAccessView(View):
    CREW_LIST = (
        "Ридли Скотт", "Энди Уир", "Марк Уотни",
        "Венката Капур", "Тедди Сандерс", "Шон Бин",
    )
    
    def dispatch_request(self) -> ft.ResponseReturnValue:
        context = {
            "crew_list": DistributionAccessView.CREW_LIST
        }

        return render_template('distribution.html', **context)
