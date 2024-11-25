from flask import Flask, render_template, request

app = Flask(__name__)
valortarro=9000
@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def promedionotas():
    nombre = None
    total = None
    descuento = 0
    valordescuento = None
    error_message = None
    resultado = None

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            edad = request.form['edad']
            cantidadtarros = request.form['cantidadtarros']

            if not nombre or not edad or not cantidadtarros:
                error_message = "Debe llenar todos los campos"
            else:
                nombre = str(nombre)
                edad = int(edad)
                cantidadtarros = int(cantidadtarros)

                if 18<= edad <=30:
                    descuento = 0.15
                elif 30 < edad:
                    descuento = 0.25
                else:
                    descuento = 0
            total = (cantidadtarros * valortarro)
            valordescuento = total * descuento
            resultado = total - valordescuento



        except ValueError:
            error_message = "Por favor, verifique ingresar texto en nombre e ingresar valores numéricos para cantidad de tarros y edad."

    return render_template('ejercicio1.html', nombre=nombre, total=total, valordescuento=valordescuento, resultado=resultado, error_message=error_message)














@app.route('/ejercicio2', methods=['GET', 'POST'])
def calcularMayor():
    name = None
    contrasena = None
    error_message = None
    mensaje = None

    if request.method == 'POST':
        try:
            name = request.form['name']
            contrasena = request.form['contrasena']

            name = str(name)
            contrasena = str(contrasena)
        except Exception as e:
            error_message = str(e)



    if name == 'juan' and contrasena == 'admin':
        mensaje = 'Bienvenido administrador Juan'
    elif name == 'pepe' and contrasena == 'user':
        mensaje = 'Bienvenido usuario Pepe'
    else:
        mensaje = 'Usuario o contraseña incorrectos'


    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run()