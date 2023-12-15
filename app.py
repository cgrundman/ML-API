import json
from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__, template_folder='templates')

employees = [{'id': 1, 'name': 'Ashley'},
             {'id': 2, 'name': 'Kate'},
             {'id': 3, 'name': 'Joe'}]


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)


@app.route('/add_employee', methods=['POST', 'GET'])
def create_employee():
    if request.method == "POST":
        # global nextEmployeeId
        # employee = json.loads(nm.data)
        # if not employ_is_valid(employee):
        #     return jsonify({'error': 'Invalid employee properties.'}), 400
        #
        # employee['id'] = nextEmployeeId
        # nextEmployeeId += 1
        # employees.append(employee)
        employee = request.form["nm"]
        return redirect()
    else:
        return render_template("add_employee.html")


# @app.route('/employees/<int:id>', methods=['PUT'])
# def update_employee(id: int):
#     employee = get_employee(id)
#     if employee is None:
#         return jsonify({'error': 'Employee does not exist.'}), 404
#
#     updated_employee = json.loads(request.data)
#     if not employee_is_valid(updated_employee):
#         return jsonify({'error': 'Invalid employee properties'}), 400
#
#     employee.update(updated_employee)
#
#     return jsonify(employee)


# @app.route('/employees/<int:id>', methods=['DELETE'])
# def delete_employee(id: int):
#     global employees
#     employee = get_employee(id)
#     if employee is None:
#         return jsonify({'error': 'Employee does not exist.'}), 404
#
#     employees = [e for e in employees if e['id'] != id]
#     return jsonify(employee), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
