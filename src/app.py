from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{"label": "My first task", "done":False},
         {"label": "My second task", "done":False}
         ]

@app.route( '/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    global todos
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(todos), 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos
    try:
        del todos[position]
        return jsonify(todos), 200
    except IndexError:
        return jsonify({"error": "Index out of range"}), 400
    


if __name__ ==  '__main__':
    app.run(host= '0.0.0.0', port=3245, debug=True)