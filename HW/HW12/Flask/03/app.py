from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route('/goodbye/')
def goodbye():
    return render_template('goodbye.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)