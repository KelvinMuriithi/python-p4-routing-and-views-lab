#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:name>')
def print_string(name):
    print(name)
    return name

@app.route('/count/<int:parameter>')
def count(parameter):
        result = ""
        for i in range(parameter):
            result += f"{i}\n"
        return result

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = float(num1)
    num2 = float(num2)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
            return str(result)  # Always return float for division
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation!'

    # Return as int string if whole number
    if result == int(result):
        return str(int(result))
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
