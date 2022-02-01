import logging
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return jsonify({'value': "I'M INDEX"})


@app.route("/get", methods=['GET', 'POST'])
def get():
    if request.method == 'GET':
        return jsonify({'value': "I'M GET"})
    return jsonify({'value': "I'M GET"})


@app.route("/get/<int:id_user>/<int:id_post>", methods=['GET'])
def get_id(id_user, id_post):
    return jsonify({'value': f"I'M USER ID {id_user}, POST ID {id_post}"})


@app.route("/post", methods=['POST'])
def post():
    var = request.get_json()
    print(var)
    print(var['algum_valor'])
    return jsonify('Sucesso'), 200 # nicolas é gato


if __name__ == '__main__':
    app.run(debug=True)