from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return f'Olá, {name}!'

@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1, num2):
    return f'A soma é {num1} e {num2}'

if __name__ == '__main__':
    app.run(debug=True)
