from flask import Flask, request, Response, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    data = dict(
        path=request.path,
        referrer = request.referrer,
        content_type=request.content_type,
        method=request.method    
    )
    return "<a href='/posts'>Posts 2</a>"

@app.route('/response')
def response():
    return render_template('response.html')

@app.route('/redirect')
def redirect_func():
    return redirect(url_for('response'))

@app.route('/posts')
@app.route('/posts/<int:id>')
def posts(id):
    titulo = request.args.get("titulo")
    data = dict(
        path=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        titulo=titulo,
        id=id if id else 0
    )
    return data




if __name__ == '__main__':
    app.run(debug=True)