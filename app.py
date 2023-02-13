from flask import Flask, url_for, request, render_template


app = Flask(__name__)

app.config["SECRET_KEY"] = "my_super_puoer_secret_key"
app.config["DEBUG"] = True
