from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    numero_1 = request.args.get('numero1', None)
    numero_2 = request.args.get('numero2', None)
    operacao = request.args.get('operacao', None)
    if not numero_1 or not numero_2 or not operacao:
    return jsonify({
    'mensagem': "Por favor envie dois numeros, e a operacao que deseja realizar.",
    'operacao': 'divisao, multiplicacao'
    })
    
    else:
    if operacao == 'divisao':
      return jsonify({
        'resultado': int(numero_1) / int(numero_2)
      })
    elif operacao == 'multiplicacao':
      return jsonify({
        'resultado': int(numero_1) * int(numero_2)
      })
    else:
    return jsonify({'resultado':resultado})
    
if__name__=="__main__":
    app.run(debug=True)