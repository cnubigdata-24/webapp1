from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask CI/CD on MS Azure (0105_1553) !!! Success"
