from flask import Flask, request, render_template, url_for
import sqlite3


app = Flask(__name__)


def get_db():
    conn = sqlite3.connect('crud.db')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)'
    )
    return conn


def item_exists(item_id):
    conn = get_db()
    item = conn.execute(
        'SELECT * FROM items WHERE id = ?', (item_id,)
    ).fetchone()
    conn.close()
    return item


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name'].strip()
    conn = get_db()
    conn.execute('INSERT INTO items (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return render_template(
        'result.html',
        message=f'Добавлено: {name}',
        back_url=url_for('home')
    )


@app.route('/items')
def items():
    conn = get_db()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('items.html', items=items)


@app.route('/delete', methods=['POST'])
def delete():
    item_id = int(request.form['id'])
    if not item_exists(item_id):
        return render_template(
            'result.html',
            message=f'Ошибка: запись с ID {item_id} не найдена',
            back_url=url_for('home')
        )
    conn = get_db()
    conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return render_template(
        'result.html',
        message=f'Удален ID: {item_id}',
        back_url=url_for('home')
    )


@app.route('/update', methods=['POST'])
def update():
    item_id = int(request.form['id'])
    new_name = request.form['name'].strip()
    if not item_exists(item_id):
        return render_template(
            'result.html',
            message=f'Ошибка: запись с ID {item_id} не найдена',
            back_url=url_for('home')
        )
    conn = get_db()
    conn.execute(
        'UPDATE items SET name = ? WHERE id = ?',
        (new_name, item_id)
    )
    conn.commit()
    conn.close()
    return render_template(
        'result.html',
        message=f'Обновлен ID {item_id}: {new_name}',
        back_url=url_for('home')
    )


app.run()
