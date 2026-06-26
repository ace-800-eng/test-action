#!/usr/bin/env python3
"""
Simple Calculator Web Application
Performs basic arithmetic operations: addition, subtraction, multiplication, division
"""

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f0f0f0; }
        .calculator { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); width: 300px; }
        h2 { text-align: center; color: #333; }
        input { width: 100%; padding: 10px; margin: 8px 0; box-sizing: border-box; border: 1px solid #ccc; border-radius: 5px; font-size: 16px; }
        .buttons { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px; }
        button { padding: 12px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; background: #4CAF50; color: white; }
        button:hover { background: #45a049; }
        #result { margin-top: 15px; padding: 10px; background: #e8f5e9; border-radius: 5px; text-align: center; font-size: 18px; font-weight: bold; color: #333; min-height: 40px; }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>🧮 Simple Calculator</h2>
        <input type="number" id="num1" placeholder="Enter first number" />
        <input type="number" id="num2" placeholder="Enter second number" />
        <div class="buttons">
            <button onclick="calc('add')">➕ Add</button>
            <button onclick="calc('subtract')">➖ Subtract</button>
            <button onclick="calc('multiply')">✖️ Multiply</button>
            <button onclick="calc('divide')">➗ Divide</button>
        </div>
        <div id="result">Result will appear here</div>
    </div>

    <script>
        async function calc(operation) {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);

            if (isNaN(num1) || isNaN(num2)) {
                document.getElementById('result').innerText = '⚠️ Please enter valid numbers';
                return;
            }

            const response = await fetch('/calculate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ num1, num2, operation })
            });

            const data = await response.json();
            document.getElementById('result').innerText = '= ' + data.result;
        }
    </script>
</body>
</html>
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


@app.route('/')
def home():
    return render_template_string(HTML)


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        result = "Error: koi sahi number add kro"

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)