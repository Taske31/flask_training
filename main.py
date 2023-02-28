from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    db_sess = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess.add(user)

    user = User()
    user.surname = "Daniel"
    user.name = "Karikh"
    user.age = 17
    user.position = "main engeneer"
    user.speciality = "engineer"
    user.address = "module_3"
    user.email = "sasdadasdasdsad@mars.org"
    db_sess.add(user)

    user = User()
    user.surname = "Michael"
    user.name = "Trotsky"
    user.age = 45
    user.position = "cook"
    user.speciality = "main cook"
    user.address = "module_2"
    user.email = "cook_mars@mars.org"
    db_sess.add(user)

    user = User()
    user.surname = "Pluto"
    user.name = "Rigulas"
    user.age = 41
    user.position = "doctor"
    user.speciality = "main engineer"
    user.address = "module_4"
    user.email = "h2o@mars.org"
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
