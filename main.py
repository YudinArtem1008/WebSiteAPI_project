import datetime
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user
from data import db_session
from data.sites import Sites
from data.users import User
from forms.login import LoginForm
from forms.register import RegisterForm
from forms.search import SearchingForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/', methods=['GET', 'POST'])
def main():
    url = url_for('static', filename='css/style.css')
    form = SearchingForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        res = db_sess.query(Sites).filter((Sites.hypertext.contains(form.searching_label.data)) |
                                          (Sites.about.contains(form.searching_label.data))).all()
        if form.speech_moving.data:
            return redirect('/speak')
        return render_template('search.html', sites=res, url=url, form=form)
    return render_template("main_window.html", url=url, form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', form=form,
                                   message="Пароли не совпадают", title="Регистрация")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', form=form,
                                   message="Такой пользователь уже есть", title="Регистрация")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    url = url_for('static', filename='css/style_for_forms.css')
    return render_template('register.html', form=form, url=url, title="Регистрация")


@app.route('/login', methods=['GET', 'POST'])
def login():
    url = url_for('static', filename='css/style_for_forms.css')
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form, url=url)
    return render_template('login.html', title='Авторизация', form=form, url=url)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/speak', methods=['GET', 'POST'])
@login_required
def speak():
    url = url_for('static', filename='css/style.css')
    form = SearchingForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template("speech_search.html", form=form, url=url)


if __name__ == '__main__':
    db_session.global_init("db/browser.db")
    app.run(port=5000, host='127.0.0.1')
