from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    numero_1 = request.args.get('numero1', None)
    numero_2 = request.args.get('numero2', None)
    operacao = request.args.get('operacao', None)
    if not numero_1 or not numero_2 or not operacao:
    return jsonify({
      'mensagem': "Envie dois numeros, e se desejar multiplicar ou dividir.",
      'ajuda': "?numero1=X&numero2=X&operacao=X",
      'operacoes': 'multiplicar''dividir'
    })
    else:
    if operacao == 'multiplicar':
      return jsonify({
        'resultado': int(numero_1) * int(numero_2)
      })
    if operacao == 'dividir':
      return jsonify({
        'resultado': int(numero_1) / int(numero_2)
      })
    else:
      return jsonify({
        'erro': 'operacao nao encontrada',
      })

if __name__ == "__main":
app.run(debug=True)