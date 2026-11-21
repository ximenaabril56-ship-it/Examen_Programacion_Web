from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
   if request.method == 'POST':
       nombre = request.form['nombre']
       edad = int(request.form['edad'])
       cantidad = int(request.form['cantidad'])

       total = cantidad * 9000

       if edad < 18:
           porcentaje = 0
       elif 18 <= edad <= 30:
           porcentaje = 0.15
       else:
              porcentaje = 0.25
       descuento = total * porcentaje
       total_con_descuento = total - descuento

       return render_template(
           'ejercicio1.html',
            nombre=nombre,
            edad=edad,
            total=total,
            descuento=descuento,
            total_pagar=total_con_descuento
       )
   
   return render_template('ejercicio1.html')           
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
       usuario = request.form['usuario']
       contrasena = request.form['contrasena']

       if usuario == 'juan' and contrasena == 'admin':
           mensaje = 'Bienvenido administrador juan'
       elif usuario == 'pepe' and contrasena == 'user':
           mensaje = 'Bienvenido usuario pepe'
       else:
           mensaje = 'Usuario o contraseña incorrectos'

       return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')
        
if __name__ == '__main__':
    app.run(debug=True)