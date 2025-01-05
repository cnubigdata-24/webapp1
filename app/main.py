from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Hello, World! CI/CD Test with GitHub Action and MS Azure !!!\nCurrent Time: {current_time}"

