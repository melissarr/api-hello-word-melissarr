from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    numero1 = request.args.get('numero1', None)
    numero2 = request.args.get('numero2', None)
    operacao = request.args.get('operacao', None)
    if operacao == 'dividir':
      return jsonify({
        'resultado': int(numero1) / int(numero2)
      })
    if operacao == 'multiplicar':
      return jsonify({
        'resultado': int(numero1) * int(numero2)
    else: 
        resultado= "envie dois numeros e escolha se deseja dividir ou multiplicar"
    return jsonify({'resultado': resultado})
      })
if__name__=="__main__":
    app.run(debug=True)