import datetime
from data import db_session
from data.__all_models import *
from flask import (Flask, url_for, request, render_template)
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'


def main():
    db_session.global_init("db/colonisation_db.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    team_leaders = {}
    for job in jobs:
        team_leader = db_sess.query(User).filter(User.id == job.team_leader).first()
        team_leaders[job.id] = team_leader.name + ' ' + team_leader.surname
    return render_template("jobs.html", jobs=jobs, team_leaders=team_leaders)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
