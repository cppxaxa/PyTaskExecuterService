from flask import Flask
from flask_restful import Resource, Api
import threading
from Draw import DrawProcess

process = DrawProcess()
process.SetPayload("for i in range(50):\n\tprint(i+1)")

task = threading.Thread(target=process.Draw, args=(False, False, 1))
task.start()

app = Flask(__name__)
api = Api(app)

class TaskServer(Resource):
    def get(self):
        return {'hello': 'world'}, 200
    def post(self):
        return "AckP", 200
    def delete(self):
        return "AckD", 200

api.add_resource(TaskServer, '/task')

app.run(host = "0.0.0.0")