"""Utworzenie prostej witryny na localhost + parę funkcji"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def test():
    return 'Witaj!'


@app.route('/innastrona')
def innastrona():
    return 'Witaj na innej stronie!'


@app.route('/klient/<numer>')
def klient(numer):
    return f"Witaj kliencie o numerze {numer}!"


@app.route('/dodaj/<zmienna1>+<zmienna2>')
def dodaj(zmienna1, zmienna2):
    suma = int(zmienna1) + int(zmienna2)
    return f"Wynik dodawania wynosi: {suma}"


@app.route('/index')
def go_to_index():
    return render_template('index.html', zm='Wojtek Ziarnik')


if __name__ == '__main__':
    app.run(debug=True)
