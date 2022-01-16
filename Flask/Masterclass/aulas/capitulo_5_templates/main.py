from flask import flash, Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret' 


@app.route('/templates')
def templates():
    users = {
        'name': 'lucas',
        'age': '22',
        'email': 'lucas@gmail.com'
    }
    
    flash('This is a flash message')

    return render_template('templates.html', users=users)

@app.route('/users')
def users():

    flash('Users flash message')   
    
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)