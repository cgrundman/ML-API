# import json
from flask import Flask, jsonify  # , request, render_template, redirect

app = Flask(__name__, template_folder='templates')

employees = [{'id': 1, 'name': 'Ashley'},
             {'id': 2, 'name': 'Kate'},
             {'id': 3, 'name': 'Joe'}]


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)  # TODO return list


@app.route('/ai', methods=['GET'])
def ai():
    return jsonify(employees)  # TODO (simple example from ai model)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
