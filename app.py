from flask import Flask


app = Flask(__name__)

app.config["SECRET_KEY"] = "my_super_puoer_secret_key"
app.config["DEBUG"] = True
