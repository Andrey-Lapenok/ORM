from data import db_session
from data import __all_models
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = __all_models.User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    for i in range(3):
        user = __all_models.User()
        user.surname = "Sailor " + str(i)
        user.name = "Muller"
        user.age = 20 + i
        user.position = "Sailor"
        user.speciality = "Meal"
        user.address = "module_" + str(i)
        user.email = f"sailor_{i}@mars.org"
        db_sess.add(user)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
