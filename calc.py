import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calculadora.html')

@app.route('/calcula', methods=['POST'])
def calculaWeb():
    valor1 = request.form['num1']
    valor2 = request.form['num2']
    operador = request.form['operador']

    v1 = int(valor1)
    v2 = int(valor2)

    if(operador == 'soma'):
        resultado = v1 + v2
    elif(operador == 'subtração'):
        resultado = v1 - v2
    elif(operador == 'multiplicação'):
        resultado = v1 * v2
    elif(operador == 'divisão'):
        if v1 == 0 or v2 == 0:
            resultado = 'Divisor e dividendo não podem ser zero!'
        else:
            resultado = v1 / v2

    return str(resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
