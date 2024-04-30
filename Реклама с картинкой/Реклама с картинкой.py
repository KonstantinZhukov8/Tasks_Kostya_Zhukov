from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main_page():
    return ''


@app.route('/promotion_image')
def promotion_image():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Колонизация</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
              rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src='{url_for('static', filename='img/mars.png')}'>
        <div class="alert alert-dark" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-success" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-secondary" role="alert">
            Мы сделаем обитаемыми безжиненные пока планеты.
        </div>
        <div class="alert alert-warning" role="alert">
            И начнем с Марса!
        </div>
        <div class="alert alert-danger" role="alert">
            Присоединяйся!
        </div>
    </body>
    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
