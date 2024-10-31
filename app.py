from flask import Flask

app = Flask(__name__)

def suma(a, b):
    return a + b

@app.route('/')
def hello():
    result = suma(5, 3)
    return f"La suma de 5 y 3 es: {result}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
