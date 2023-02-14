from flask import Flask


app = Flask(__name__)

app.config["SECRET_KEY"] = "my_super_puper_secret_key"
app.config["DEBUG"] = True
