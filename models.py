from db import tasks_collection
from bson import ObjectId

class TaskModel:
    @staticmethod
    def add_task(task_data):
        result = tasks_collection.insert_one(task_data)
        return str(result.inserted_id)
        
    @staticmethod
    def get_task_by_id(task_id):
        try:
            task = tasks_collection.find_one({"_id": ObjectId(task_id)})
            if task:
                task['_id'] = str(task['_id'])
            return task
        except:
            return None
    @staticmethod
    def get_tasks():
        tasks=list(tasks_collection.find())
        for task in tasks:
            task['_id']=str(task['_id'])
        return  tasks
    @staticmethod
    def update_task(task_id, updated_data):
        try:
            result = tasks_collection.update_one(
                {"_id": ObjectId(task_id)},
                {"$set": updated_data}
            )
            return result.modified_count > 0
        except:
            return False
    @staticmethod
    def delete_task(task_id):
        try:
            result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
            return result.deleted_count > 0
        except:
            return False