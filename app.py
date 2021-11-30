# test 1

from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def root():
    db = sqlite3.connect('books.db')
    cursor = db.cursor()

    data = cursor.execute('SELECT * FROM books').fetchall()

    db.close()

    return str(data)


@app.route('/add')
def add():
    db = sqlite3.connect('books.db')
    cursor = db.cursor()

    name = request.args.get('name')
    page = request.args.get('page')

    cursor.execute('INSERT INTO books(name,page) VALUES ("%s", "%s")' % (name, page))
    db.commit()

    db.close()

    return '%s added' % name


@app.route('/update/<_id>')
def update(_id):
    db = sqlite3.connect('books.db')
    cursor = db.cursor()

    name = request.args.get('name')
    page = request.args.get('page')

    cursor.execute('UPDATE books SET name = "%s", page = "%s" WHERE id = "%s" ' % (name, page, _id))
    db.commit()

    db.close()

    return '%s updated' % _id


@app.route('/delete/<_id>')
def delete(_id):
    db = sqlite3.connect('books.db')
    cursor = db.cursor()

    cursor.execute('DELETE FROM books WHERE id = "%s"' % _id)
    db.commit()

    db.close()

    return '%s deleted' % _id


@app.route('/select/<_id>')
def select(_id):
    db = sqlite3.connect('books.db')
    cursor = db.cursor()

    data = cursor.execute('SELECT * FROM books WHERE id = "%s"' % _id).fetchall()

    db.close()
    return str(data)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
