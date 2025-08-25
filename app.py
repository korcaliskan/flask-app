from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from config import Config
from models import db, User, Member

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Üretimde hash kullanılmalı
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Kullanıcı adı veya şifre hatalı')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    total_members = Member.query.count()
    total_aidat = db.session.query(db.func.sum(Member.aidat_total)).scalar() or 0
    return render_template('dashboard.html', total_members=total_members, total_aidat=total_aidat)

@app.route('/members')
@login_required
def members():
    members_list = Member.query.all()
    return render_template('members.html', members=members_list)

if __name__ == '__main__':
    app.run(debug=True)
