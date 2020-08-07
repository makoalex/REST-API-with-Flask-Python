from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "1st one Mako"
app.run(port=5000)