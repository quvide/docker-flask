from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Everything working as intended, you're ready to configure more!"
