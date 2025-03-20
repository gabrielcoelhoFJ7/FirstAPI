from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/<name>')
def hello_name(name):
    return f'Olá, {name}!'


@app.route('/soma/<num1>/<num2>')
def soma(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return f'A soma é {num1 + num2}!'
    except ValueError:
        return jsonify({'erro': 'Formato inválido'})

@app.route('/sub/<num1>/<num2>')
def sub(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return f'A subtração é {num1 - num2}!'
    except ValueError:
        return jsonify({'erro': 'Formato inválido'})


@app.route('/div/<num1>/<num2>')
def div(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return f'A divisão é {num1 / num2}!'
    except ValueError:
        return jsonify({'erro': 'Formato inválido'})


@app.route('/mult/<num1>/<num2>')
def mult(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return f'A multiplicação é {num1 * num2}!'
    except ValueError:
        return jsonify({'erro': 'Formato inválido'})

@app.route('/par/<num1>')
def par(num1):
    try:
        num1 = float(num1)
        if num1 % 2 == 0:
            return f'O número {num1} é par!'
        else:
            return f'O número {num1} é impar!'
    except ValueError:
        return jsonify({'erro': 'Formato inválido'})

if __name__ == '__main__':
    app.run(debug=True)
