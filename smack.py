from flask import Flask, render_template, redirect, url_for
import config
from models import User
from exts import db


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return

@app.route('/register/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.username == username).first()
        if user:
            return 'username already used'
        else:
            if password1 != password2:
               return 'password not same'
            else:
                user = User(username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
