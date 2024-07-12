from flask import Flask, render_template, request
from controladores.controlador_ropa import ControladorRopa
from dao.dao_ropa import RopaDAO
from dominio.ropa import Ropa
from servicios.servicio_orden import ServicioOrden

app = Flask(__name__)
controlador_ropa = ControladorRopa()
servicio_orden = ServicioOrden()

@app.route('/')
def index():
    ropa = controlador_ropa.obtener_toda_ropa()
    return render_template('index.html', ropa=ropa)

@app.route('/orden', methods=['POST'])
def orden():
    nombre_ropa = request.form['nombre_ropa']
    cantidad = int(request.form['cantidad'])
    if servicio_orden.procesar_orden(nombre_ropa, cantidad):
        return "¡Orden realizada con éxito!"
    else:
        return "Fallo al realizar la orden. Por favor, verifica la disponibilidad."

if __name__ == '__main__':
    app.run(debug=True)
