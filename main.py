from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to IndiePoetry!"

if __name__ == '__main __':
    app.run(host='0.0.0.0')