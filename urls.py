from app import app
from flask import send_from_directory

import views


app.add_url_rule("/<string:title>", view_func=views.IndexView.as_view("index"))
app.add_url_rule("/index/<string:title>", view_func=views.IndexView.as_view("index1"))

app.add_url_rule("/training/<string:prof>", view_func=views.TrainingView.as_view("training"))
app.add_url_rule("/list_prof/<string:list>", view_func=views.ProfListView.as_view("prof_list"))

app.add_url_rule("/answer", view_func=views.SurveyView.as_view("survey"))
app.add_url_rule("/emergency-access", view_func=views.EmergencyAccessView.as_view("emergency_access"))

app.add_url_rule("/distribution", view_func=views.DistributionView.as_view("distribution"))

app.add_url_rule("/table/<string:sex>/<int:age>", view_func=views.TableView.as_view("table"))

app.add_url_rule("/gallery", view_func=views.LandscapeGalleryView.as_view("gallery"))
app.add_url_rule("/media/<string:filename>", view_func=views.MediaView.as_view("media_gallery"))

app.add_url_rule("/member", view_func=views.MemberView.as_view("member"))
