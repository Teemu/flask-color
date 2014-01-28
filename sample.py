from flask import Flask, redirect
import flask.ext.color

app = Flask(__name__)
app.config['DEBUG'] = True
flask.ext.color.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    import time
    time.sleep(0.7)
    return """
<html>
<img src="/favicon.ico" />
<img src="/static/graphics.png" />
<img src="/static/style.css" />
<img src="/static/theme.css" />
<img src="/static/awesome.css" />
<img src="/auth/users/login" />
<img src="/callback" />
<form action="/" method="post">
    <input type="submit" />
</form>

</html>
"""

@app.route('/auth/users/login')
def r():
    return 'Hello World!'

@app.route('/static/<example>')
def lol(example):
    return 'Hello World!'

@app.route('/callback')
def asd():
    return redirect('/static/fffefe')

if __name__ == '__main__':
    app.run()