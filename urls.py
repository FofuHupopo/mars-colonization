from app import app

import views


app.add_url_rule("/<string:title>", view_func=views.IndexView.as_view("index"))
app.add_url_rule("/index/<string:title>", view_func=views.IndexView.as_view("index1"))

app.add_url_rule("/training/<string:prof>", view_func=views.TrainingView.as_view("training"))
app.add_url_rule("/list_prof/<string:list>", view_func=views.ProfListView.as_view("prof_list"))
