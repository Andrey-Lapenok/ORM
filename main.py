import datetime
from data import db_session
from data.__all_models import *
from flask import (Flask, url_for, request, render_template)

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


if __name__ == '__main__':
    main()
