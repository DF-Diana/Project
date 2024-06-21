from flask import Flask, render_template, request;
from math import sqrt
from operaciones import OperasBas
from traductor import traductorIngEsp, buscarPalabra, agregarPalabra
from cine import cine

app=Flask(__name__)


@app.route("/")
def index():
    titulo = "PRACTICAS - IEVN903" 
    return render_template("index.html", titulo=titulo)


#distancia entre dos puntos
@app.route("/formulario2", methods=["GET"])
def form2():
    return render_template("formulario2.html")
@app.route("/resultado2", methods=["POST"])
def resultado2():
    x1 = float(request.form.get("x1"))
    x2 = float(request.form.get("x2"))
    y1 = float(request.form.get("y1"))
    y2 = float(request.form.get("y2"))
    res2 = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return render_template("resultado2.html", x1=x1, x2=x2, y1=y1, y2=y2, res2=res2)

#FORMULARIO 3 GRADOS 
@app.route("/formulario3", methods=["GET"])
def form3():
    return render_template("formulario3.html")
@app.route("/resultado3", methods=["POST"])
def resultado3():
    n = float(request.form.get("n"))
    cambio = request.form.get("cambio")

    if cambio == "celsius":
        res3 =((n - 32) * 5.0/9.0)
        tipo = "Fahrenheit >> Celsius"
    elif cambio == "fahrenheit":
        res3 = ((n * 9.0/5.0) + 32)
        tipo = "Celsius >> Fahrenheit"

    return render_template("resultado3.html", n=n, res3=res3, tipo=tipo)

#OPERACIONES
@app.route("/formulario", methods=["GET", "POST"])
def operacines():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        operacion = request.form.get("operacion")

        obj = OperasBas()
        obj.num1 = num1
        obj.num2 = num2

        if operacion == "suma":
            res = obj.suma()
        elif operacion == "resta":
            res = obj.resta()
        elif operacion == "multi":
            res = obj.multi()
        elif operacion == "div":
            res = obj.div()

        return render_template("formulario.html", res=res)
    else:
        return render_template("formulario.html")
    
#TRADUCTOR
@app.route("/formulario1", methods=["GET", "POST"])
def traductor():

    if request.method == "POST":
        
        if request.form.get("btn1") == "Registrar":
            espanol = request.form.get("word1")
            ingles = request.form.get("word2")
            agregarPalabra(espanol, ingles)

        if request.form.get("btn02") == "Traducir":
            palabra = request.form.get("palabra")
            idioma = request.form.get("idioma")
            palabras = buscarPalabra()
            traduccion = palabras.get(palabra, "No se encontró la palabra")
            return render_template("formulario1.html", palabra=palabra, traduccion=traduccion)
    
    return render_template("formulario1.html")

#COMPRA DE BOLETOS
@app.route("/formulario4", methods=["GET", "POST"])
def compraBoleto():
    if request.method == "POST":
        name = request.form.get("name")
        numPersonas = int(request.form.get("numPersonas"))
        numBoletos = int(request.form.get("numBoletos"))
        tarjeta = request.form.get("tarjeta")

        compra = cine()
        compra.name = name
        compra.numPersonas = numPersonas
        compra.numBoletos = numBoletos
        compra.tarjeta = tarjeta
        

        compra.totalInicial()
        compra.agregarCompra()

        return render_template("resultado4.html", name=compra.name, numPersonas=compra.numPersonas, numBoletos=compra.numBoletos, tarjeta=compra.tarjeta, total=compra.total)
    return render_template("formulario4.html")

@app.route("/tablaClientes", methods=["GET", "POST"])
def tablaClientes():
    compras = cine.buscarCompra()
    comprasFiltro = []
    cliente = ""
    if request.method == "POST":
        cliente = request.form.get("cliente")
        comprasFiltro = [compra for compra in compras if compra[0] == cliente]
    else:
        comprasFiltro = list(compras)

    return render_template("tablaClientes.html", cliente=cliente, compras=comprasFiltro)


if __name__=="__main__":
    app.run(debug=True)

 