from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    numero_1 = request.args.get('numero1', None)
    numero_2 = request.args.get('numero2', None)
    operacao = request.args.get('operacao', None)
    return jsonify({
        'mensagem': "Por favor envie dois numeros, e se deseja realizar a operacao multiplicar ou dividir.",
        'operacao': 'dividir, multiplicar'
    })
    else:
    if operacao == 'dividir':
      return jsonify({
        'resultado': int(numero_1) / int(numero_2)
      })
    elif operacao == 'multiplicar':
      return jsonify({
        'resultado': int(numero_1) * int(numero_2)
      })
    else:
    return jsonify({'resultado':resultado})
    
if__name__=="__main__":
    app.run(debug=True)