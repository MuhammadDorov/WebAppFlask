from DBandImports import *

@app.route("/")
@app.route("/index")
def index():
    print(url_for('index'))
    info = []
    try:
        info = EmployeesCatalog.query.all()
    except:
        print("Ошибка чтения из БД")
    return render_template('index.html', list=info, title='Главная страница')


@app.route("/addemploy", methods=["POST", "GET"])
def addemploy():
    if request.method == "POST":
        # здесь должна быть проверка корректности введенных данных
        # try:
            lfname = request.form['lfname']
            post = request.form['post']
            wages = request.form['wages']
            adddate = request.form['adddate']
            employ = EmployeesCatalog(lfname, post, wages, adddate)
            db.session.add(employ)
            db.session.commit()
        # except:
        #     print("Ошибка добавления в БД")
    return render_template("add_employees.html", title="Добавление нового сотрудника")


# обработчик для несуществующих страниц
@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title="404 Ошибка")


if __name__ == '__main__':
    app.run(debug=True)
