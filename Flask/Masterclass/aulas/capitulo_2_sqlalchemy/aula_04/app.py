from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.name


@app.route("/")
def index():
    users = User.query.all()
    return render_template('user.html', users=users)


@app.route("/user/delete/<int:id>")
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.remove(user)
    db.session.commit()

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)