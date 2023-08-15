import os
from flask import Flask, jsonify, send_from_directory, render_template, redirect

from funcs.sum import sumarValores


app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


@app.route('/')
def home():
    return render_template('index.html')


'''
Comentado para que no se pueda acceder a las rutas
'''
@app.route('/objectJS/<valores>')
def objectJS(valores):
    #transform valores to list
    valores = valores.replace("[", "")
    valores = valores.replace("]", "")
    valores = valores.split(",")
    valores = [int(i) for i in valores]

    return jsonify(sumarValores(valores))




@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')


if __name__ == "__main__":
    app.run(port=port)
