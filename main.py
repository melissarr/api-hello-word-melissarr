from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
p= 0
 i= 0
    valor= int(input("Digite um valor:"))
    if valor % 2 == 0
        p= valorelse:
        i= valor
    print(f'Ovalor de p é: {p}')
    print(f'Ovalor de i é: {i}')
    
    return jsonify({'resultado':resultado})
if__name__=="__main__":
    app.run(debug=True)