from flask import Flask, render_template, request, abort


app = Flask(__name__)

@app.errorhandler(400)
def spatny_pozadavek(chyba):
    return "Tohle nejde pocitat", 400

@app.errorhandler(404)
def neni_obsah(chyba):
    return "Not found", 404

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("kalkulacka.html")
    elif request.method == 'POST':
        vsechny_operace = {
            'plus': ('+', lambda x, y: x + y),
            'minus': ('-', lambda x, y: x - y),
            'krat': ('x', lambda x, y: x * y),
            'deleno': ('/', lambda x, y: x / y),
        }

        try:
            prvni = int(request.form['prvni'])
            druhe = int(request.form['druhe'])
        except ValueError:
            abort(400)

        operace = request.form['operace']
        symbol, fce = vsechny_operace[operace]
        vysledek = fce(prvni, druhe)
        return render_template('vysledek.html', prvni = prvni, druhe=druhe, symbol=symbol, vysledek=vysledek)
