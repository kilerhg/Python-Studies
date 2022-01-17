from flask import flash, Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret' 


@app.route('/templates')
def templates():
    
    
    flash('This is a flash message')

    return render_template('templates.html')

@app.route('/users')
def users():

    flash('Users flash message')  
    users = [{
        'name': 'lucas',
        'age': '22',
        'email': 'lucas@gmail.com'
    },
    {
        'name': 'KILERHG',
        'age': '19',
        'email': 'kilerhg@gmail.com'
    }
    ] 
    
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)