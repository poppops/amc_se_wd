from flask import Flask, render_template;

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello, World!'

@app.route('/test')
@app.route('/test/<title>')
def test(title=None):
    return render_template('template.html', title=title)