from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    numero_1 = request.args.get('numero1', None)
    numero_2 = request.args.get('numero2', None)
    operacao = request.args.get('operacao', None)

    if operacao == 'soma':
      return jsonify({
        'resultado': int(numero_1) + int(numero_2)
      })
    elif operacao == 'subtracacao':
      return jsonify({
        'resultado': int(numero_1) - int(numero_2)
      })
    elif operacao == 'divisao':
      return jsonify({
        'resultado': int(numero_1) / int(numero_2)
      })
    elif operacao == 'multiplicacao':
      return jsonify({
        'resultado': int(numero_1) * int(numero_2)
      })
    else:
        resultado = "enive dois numeros e se deseja dividir ou multiplicar."
      return jsonify({'resultado': resultado})
      })

if __name__ == "__main":
app.run(debug=True)