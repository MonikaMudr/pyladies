# webpiskvorky.py

# Spouštění (v příkazové řádce):
# export FLASK_APP=webpiskvorky.py
# export FLASK_DEBUG=1
# flask run

# (na Windows "set" místo "export")

from flask import Flask, render_template, request

from util import tah
from ai import tah_pocitace

app = Flask(__name__)

@app.route('/')
def hra():
    if 'pole' in request.args:
        pole = request.args['pole']
    else:
        pole = '-' * 20
    if 'cislo' in request.args:
        cislo_policka = int(request.args['cislo'])
        pole = tah(pole, cislo_policka, 'x')
        pole = tah_pocitace(pole, 'o')

    return render_template(
        'piskvorky.html',
        ocislovane_pole=enumerate(pole),
        pole=pole,
    )