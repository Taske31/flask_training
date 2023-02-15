from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def slogan():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="{url_for('static', filename='css/bootstrap.css')}" />
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img  src="{url_for('static', filename='img/mars.jpg')}"
                    alt="Здесь должен был быть Марс">
                    <p class ="alert alert-dark" role="alert">Человечество вырастает из детства.</p>
                    <p class ="alert alert-success" role="alert">Человечеству мала одна планета.</p>
                    <p class ="alert alert-light" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class ="alert alert-warning" role="alert">И начнем с Марса!</p>
                    <p class ="alert alert-danger" role="alert">Присоединяйся!</p>
                  </body>
                </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut_selection.html')

@app.route('/training/<profession>')
def training(profession):
    if 'инженер' in profession or 'строитель' in profession:
        return render_template('training.html', training='Инженерные тренажеры')
    elif 'врач' in profession:
        return render_template('training.html', training='Научные симуляторы')
    elif 'пилот' in profession:
        return render_template('training.html', training='Летательный симулятор')
    elif 'олог' in profession:
        return render_template('training.html', training='Научная лаборотория')
    else:
        return render_template('training.html', training='Нам не удалось найти\nдля вас тренажер')


@app.route('/list_prof/<table>')
def list_prog(table):
    print(1)
    return render_template('list_prof.html', table=table)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    params = {
        'title': 'test',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'Выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', params=params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


