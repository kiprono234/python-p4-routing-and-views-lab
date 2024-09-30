#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    
    print(parameter)  # Print the parameter to the console
    return parameter  # Return the parameter as plain text

@app.route('/count/<int:parameter>')
def count(parameter):
    
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'  # Add a newline at the end
    return numbers  # Return just the plain text with newlines



@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Cannot divide by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
         # returns an error if the operation is invalid

        return 'Invalid operation!', 400  

    return str(result)  # Change to return plain text only

if __name__ == '__main__':
    app.run(port=5555, debug=True)
