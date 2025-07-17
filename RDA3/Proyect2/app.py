from flask import Flask, render_template, request
from rutas import calcular_ruta

app = Flask(__name__)

# Lista de ciudades disponibles
CIUDADES = ["Ibarra", "Quito", "Santo Domingo", "Manta", "Portoviejo", "Guayaquil", "Cuenca", "Loja"]



@app.route('/', methods=['GET', 'POST'])
def home():
    ruta = costo = pasa_costera = None
    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        if origen and destino and origen != destino:
            ruta, costo, pasa_costera = calcular_ruta(origen, destino)

    return render_template('base.html', ciudades=CIUDADES, ruta=ruta, costo=costo, pasa_costera=pasa_costera)

if __name__ == '__main__':
    app.run(debug=True)
