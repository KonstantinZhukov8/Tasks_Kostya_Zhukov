from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return ''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Отбор астронавтов</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                      rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/
                      Dwwykc2MPK8M2HN"
                      crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            </head>
            <body>
            <form class="login_form" method="post">
                <h1 align="center">Анекта претендента</h1>
                <h2 align="center">на участие в миссии</h2>
    
                <input align="center" type="text" class="form-control" placeholder="Введите фамилию"
                       aria-label="Username" aria-describedby="basic-addon1">
    
                <input align="center" type="text" class="form-control" placeholder="Введите имя"
                       aria-label="Username" aria-describedby="basic-addon1"><br>
    
                <input align="center" type="text" class="form-control" placeholder="Введите адрес почты"
                       aria-label="Username" aria-describedby="basic-addon1"><br>
    
                <p>Какое у вас образование?</p>
    
                <select class="form-select" aria-label="Default select example">
                  <option value="1">Начальное</option>
                  <option value="2">Среднее</option>
                  <option value="3">Высшее</option>
                </select><br>
    
                <p>Какие у вас есть профессии?</p>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck1">
                    <label class="form-check-label" for="exampleCheck1">инженер-исследователь</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck2">
                    <label class="form-check-label" for="exampleCheck1">пилот</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck3">
                    <label class="form-check-label" for="exampleCheck1">строитель</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck4">
                    <label class="form-check-label" for="exampleCheck1">экзобиолог</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck5">
                    <label class="form-check-label" for="exampleCheck1">инженер-исследователь</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck6">
                    <label class="form-check-label" for="exampleCheck1">врач</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck7">
                    <label class="form-check-label" for="exampleCheck1">инженер по терраформированию</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck8">
                    <label class="form-check-label" for="exampleCheck1">климатолог</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck9">
                    <label class="form-check-label" for="exampleCheck1">специалист по радиационной защите</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck10">
                    <label class="form-check-label" for="exampleCheck1">астрогеолог</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck11">
                    <label class="form-check-label" for="exampleCheck1">гляциолог</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck12">
                    <label class="form-check-label" for="exampleCheck1">инженер жизнеобеспечения</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck13">
                    <label class="form-check-label" for="exampleCheck1">метеоролог</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck14">
                    <label class="form-check-label" for="exampleCheck1">оператор марсохода</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck15">
                    <label class="form-check-label" for="exampleCheck1">киберинженер</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck16">
                    <label class="form-check-label" for="exampleCheck1">штурман</label>
                </div>
    
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck17">
                    <label class="form-check-label" for="exampleCheck1">пилот дронов</label>
                </div>
    
                <div class="form-group">
                    <label for="form-check">Укажите пол</label>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                        <label class="form-check-label" for="male">
                            Мужской
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                        <label class="form-check-label" for="female">
                            Женский
                        </label>
                    </div>
                </div>
    
                <div class="form-group">
                    <label for="about">Почему вы хотите принять участие в миссии?</label>
                    <textarea class="form-control" id="about" rows="1" name="about"></textarea>
                </div>
    
                <div class="form-group">
                    <label for="photo">Приложите фотографию</label><br>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div><br>
    
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                    <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                </div>
    
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
    
            </body>
        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
