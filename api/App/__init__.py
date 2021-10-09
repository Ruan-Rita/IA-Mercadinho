from flask import Flask, request, jsonify
from App.method import Amplitude
app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/way-search", methods = ['POST'])
def waysearch():
    # SCOPO
    entrada = request.form['input'] if "input" in request.form else False
    saidas = request.form['output'] if "output" in request.form else False
    methodos = request.form['method'] if "method" in request.form else False
    limit = request.form['limit'] if "limit" in request.form else False 
    return jsonify(request.form )

    if entrada & saidas.len > 0 & methodos & limit:
        if methodos == "amplitude":
            instancia = AmplitudeMethod()
            return jsonify(instancia.amplitude(entrada, saidas))
        
        elif methodos == "profundidade":
            return jsonify(True)

        elif methodos == "prof.limitada":
            return jsonify(True)

        elif methodos == "aprofundamento":
            return jsonify(True)

        elif methodos == "bidirecional":
            return jsonify(True)

    return jsonify(dict(limit = limit, entrada = entrada, saida = saidas))
