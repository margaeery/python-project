from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def table():
    data = [
        {"id": 1, "name": "Иван", "age": 25, "city": "Москва"},
        {"id": 2, "name": "Мария", "age": 30, "city": "СПб"},
        {"id": 3, "name": "Алексей", "age": 22, "city": "Казань"}
    ]
    return render_template('table.html', users=data)


app.run()
