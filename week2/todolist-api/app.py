# import Flas from "flask"
from flask import Flask, jsonify, request  
from datetime import date
from utils import search_task

# instancia de Flask 
app = Flask(__name__) #__name__   modulo actual

#diccionario = objeto javascript
tasks = [
    {
      "id":1,
      "title":"Limpiar mi cuarto",
      "category":"Hogar",
      "priority":"Alto",
      "created_at":"2023-11-16"
    }
]

@app.route("/")
def hola_mundo():
    return jsonify({
        "message": "Hello world!"
    })


@app.route("/tasks")
def get_tasks():
    return jsonify({
        "ok":True,
        "data":tasks
    })


@app.route("/tasks/<int:task_id>") #task_id variable
def get_task(task_id):
    result = search_task(tasks,task_id)
    if result is None:
        return jsonify({
            "ok":False,
            "data":"Task not found"
        })
    
    return jsonify({
            "ok":True,
            "data":result
        })


@app.route("/tasks",methods=["POST"])
def add_task():
    task = request.json
    task["id"] = len(tasks) + 1
    task["created_at"]= date.today()
    tasks.append(task)
    return jsonify({
        "ok":True,
        "data":"Tarea creada correctamente."
    }),201
        

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
     task = search_task(tasks,task_id)
     if task is None:
         return jsonify({
             "ok":False,
             "data":"Task not found"
         })
     
     new_task = request.json #obtener el json que recibimos desde postman
     task["title"] = new_task.get("title", task["title"]) #funcion get recibe dos parametros
     task["priority"] = new_task.get("priority", task["priority"])
     task["category"] = new_task.get("category", task["category"])

     return jsonify({
         "ok":True,
         "data":"Tarea actualizada correctamente"
     })
    

if __name__ == "__main__":
    app.run(debug=True) #Por cada cambio se hace un reload
