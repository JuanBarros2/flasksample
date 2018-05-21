from flask import Blueprint, jsonify, abort, request

admin = Blueprint("admin", __name__, url_prefix="/admin")

tasks = []

@admin.route('/', methods=['GET'])
def listAllTasks():
    dictasks = tasks
    for i, task in enumerate(dictasks): task['id'] = i
    return jsonify(dictasks)

@admin.route('/', methods=['POST'])
def addTasks():
    if not request.json:
        abort(400)
    tasks.append(request.json)
    return jsonify(request.json)

@admin.route('/<id>', methods=['PUT'])
def updateTask(id):
    id = int(id)
    if len(tasks) > id:
        tasks[id]= request.json
        return jsonify(tasks[id])
    else:
        abort(404)

@admin.route('/<id>', methods=['DELETE'])
def deleteTask(id):
    id = int(id)
    if len(tasks) > id:
        tasks[id]= {}
        return jsonify(tasks[id])
    else:
        abort(404)

