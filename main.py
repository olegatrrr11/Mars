from flask import Flask, url_for

app = Flask(__name__)


@app.route('/image_mars')
def img_mars():
    return f"""<!doctype html>
                    <html lang="en">
        <title>Привет, Марс!</title>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/Mars.jpg')}" alt="Mars">
        <h1>Вот она какая, красная планета.</h1>"""


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/')
def Mars():
    return "Миссия Колонизация Марса"


@app.route('/promotion')
def index1():
    return """<!doctype html>
                <html lang="en">
    <h1>Человечество вырастает из детства.</h1> 
    <h1>Человечеству мала одна планета.</h1>
    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1> 
    <h1>И начнем с Марса!</h1>
    <h1>Присоединяйся!</h1>"""


@app.route('/promotion_image')
def index2():
    return f"""<!doctype html>
                <html lang="en">
    <title>Колонизация</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/Mars.jpg')}" alt="Mars">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <title>Привет, Яндекс!</title>
    </head>
    <div class="alert alert-dark" role="alert">
        Человечество вырастает из детства.
    </div>
    <div class="alert alert-success" role="alert">
        Человечеству мала одна планета.
    </div>
    <div class="alert alert-secondary" role="alert">
        Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-warning" role="alert">
        И начнём с Марса!
    </div>
    <div class="alert alert-danger" role="alert">
        Присоединяйся!
    </div>
    """


@app.route('/choice/<planet_name>')
def index3(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                <title> Варианты выбора</title>
                <h1>Моё предложение: {planet_name}
                <h2>Эта планета близка к Земле; </h2>
                <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
                <h2 class="alert alert-success" role="alert">
                На ней много необходимых ресурсов;
                </h2>
                <h2 class="alert alert-secondary" role="alert">
                На ней есть вода и атмосфера;
                </h2>
                <h2 class="alert alert-warning" role="alert">
                На ней есть небольшое магнитное поле;
                </h2>
                <h2 class="alert alert-danger" role="alert">
                Наконец, она просто красива!
                </h2>
                """
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def index4(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                <title> Результаты</title>
                <h1>Результаты отбора</h1>
               <h3>Претентенда на участие в миссии {nickname}:</h3>
               <link rel="stylesheet"
               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
        <h3 class="alert alert-success">Поздравляем! Ваш рейтинг после этапа {level} этапа отбора</h3>
        <h3>составляет {rating}!</h3>
        <h3 class="alert alert-warning">Желаем удачи!</h3>
"""

@app.route('/carousel')
def index5():
    return f"""<!doctype html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Пейзажи Марса</title>
                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                          crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style2.css')}">
                </head>
                <body>
                    <div>
                        <h1>Пейзажи Марса</h1>
                    </div>
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                        </ol>
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img class="d-block w-100" src="{url_for('static', filename='img/p_mars1.jpg')}" alt="First slide">
                            </div>
                            <div class="carousel-item">
                                <img class="d-block w-100" src="{url_for('static', filename='img/p_mars2.jpg')}" alt="Second slide">
                            </div>
                            <div class="carousel-item">
                                <img class="d-block w-100" src="{url_for('static', filename='img/p_mars3.jpg')}" alt="Third slide">
                            </div>
                        </div>
                        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                        </a>
                        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                        </a>
                    </div>
                    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
                </body>
                </html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')