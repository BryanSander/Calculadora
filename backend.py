from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():

    dados = request.json

    numero1 = dados["numero1"]
    numero2 = dados["numero2"]
    operacao = dados["operacao"]

    if operacao == "+":
        resultado = numero1 + numero2

    elif operacao == "-":
        resultado = numero1 - numero2

    elif operacao == "*":
        resultado = numero1 * numero2

    elif operacao == "/":
        resultado = numero1 / numero2

    return jsonify({"resultado": resultado})


app.run(debug=True)