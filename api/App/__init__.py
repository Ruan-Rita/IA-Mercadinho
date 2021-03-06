from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from App.method import Amplitude,Bidirecional,Profundidade,ProfundidadeLimitada,ProfundidadeIterativo,Estrela,Greedy,CustoUniforme
import json



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def index():
    return "<p>Hello, World!</p>"

@app.route("/way-search", methods = ['POST'])
@cross_origin()
def waysearch():
    # SCOPO
    entrada = request.form['input'] if "input" in request.form else False
    saidas = list(json.loads(request.form['output'])) if "output" in request.form else False
    method = request.form['method'] if "method" in request.form else False
    limit = request.form['limit'] if "limit" in request.form else False 

    print("saidas")
    print(saidas)
    print("entrada")
    print(entrada)

    if entrada and len(saidas) > 0 and method and limit:
        if method == "amplitude":
            print("Entriasdsada dasj djka sjldlkas kldajksldjlka -*****")
            instancia = Amplitude.AmplitudeMethod()
            resultado = instancia.amplitude(entrada, saidas)
            return json.dumps(resultado)

        elif method == "profundidade":
            print("Entriasdsada dasj djka sjldlkas kldajksldjlka -*****")
            instancia = Profundidade.ProfundidadeMethod()
            resultado = instancia.profundidade(entrada, saidas)
            return json.dumps(resultado)

        elif method == "profundidade-limitada":
            print("Entriasdsada dasj djka sjldlkas kldajksldjlka -*****")
            instancia = ProfundidadeLimitada.ProfundidadeLimitadaMethod()
            resultado = instancia.profundidadeLimitada(entrada, saidas[0], int(limit))
            return json.dumps(resultado)

        elif method == "aprofundamento":
            print("Entriasdsada dasj djka sjldlkas kldajksldjlka -*****")
            instancia = ProfundidadeIterativo.ProfundidadeIterativoMethod()
            resultado = instancia.aprofundamentoIterativo(entrada, saidas[0])
            return json.dumps(resultado)

        elif method == "bidirecional":
            print("Entriasdsada dasj djka sjldlkas kldajksldjlka -*****")
            instancia = Bidirecional.BirecionalMethod()
            resultado = instancia.bidirecional(entrada, saidas[0])
            return json.dumps(resultado)

        elif method == "estrela":
            print("Entriasdsada dasj djka sjldlkas kldajksldjlka -*****")
            instancia = Estrela.EstrelaMethod()
            resultado = instancia.a_estrela(entrada, saidas[0])
            return json.dumps(resultado)

        elif method == "greedy":
            print("Entriasdsada dasj djka sjldlkas kldajksldjlka -*****")
            instancia = Greedy.GreedyMethod()
            resultado = instancia.greedy(saidas[0], entrada)
            return json.dumps(resultado)

        elif method == "custo-uniforme":
            print("Entriasdsada dasj djka sjldlkas kldajksldjlka -*****")
            instancia = CustoUniforme.CustoUniformeMethod()
            resultado = instancia.custo_uniforme(entrada, saidas[0])
            return json.dumps(resultado)

    return jsonify(dict(limit = limit, entrada = entrada, saida = saidas, method = method))
