from flask import Blueprint, request, jsonify
from models import TaskModel

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route("/addTask", methods=["POST"])
def add_task():
    task_data = request.json
    if not task_data or "title" not in task_data:
        return {"error": "bad request!!"}, 400
    task_id = TaskModel.add_task(task_data)
    return {"message": "Task added successfully", "task_id": task_id}, 201

@routes_blueprint.route("/tasks", methods=["GET"])
def retrieve_tasks():
    tasks = TaskModel.get_tasks()
    return jsonify(tasks)

@routes_blueprint.route("/updateTask/<task_id>", methods=["POST"])
def update_task(task_id):
    task_data = request.json
    if not task_data:
        return {"error": "No data provided"}, 400
    success = TaskModel.update_task(task_id, task_data)
    if not success:
        return {"error": "Task not found or update failed"}, 404
    return {"message": "Task updated successfully"}
@routes_blueprint.route("/deleteTask/<task_id>",methods=["DELETE"])
def delete_task(task_id):
    success=TaskModel.delete_task(task_id)
    if not success:
        return {"error":"Task not found or deletion failed"},500
    return {"message":"deleted successfully!"},200