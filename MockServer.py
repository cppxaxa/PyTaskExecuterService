from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

class TaskServer(Resource):
    def get(self):
        return {'hello': 'world'}, 200
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Fbp', type=list, action='append')
        parser.add_argument('RunOnce', type=bool)
        parser.add_argument('InfiniteLoop', type=bool)
        parser.add_argument('LoopLimit', type=int)
        parser.add_argument('ReturnResult', type=bool)
        args = parser.parse_args()
        
        # RunOnce = args["RunOnce"]
        # InfiniteLoop = args["InfiniteLoop"]
        # LoopLimit = args["LoopLimit"]
        ReturnResult = args["ReturnResult"]
        
        if ReturnResult == False:
            a = 10
        else:
            result = '[{"label":"cow","bottomright":{"y":354,"x":186},"topleft":{"y":267,"x":67},"confidence":0.5488251},{"label":"dog","bottomright":{"y":343,"x":209},"topleft":{"y":281,"x":122},"confidence":0.13515499},{"label":"horse","bottomright":{"y":365,"x":239},"topleft":{"y":260,"x":97},"confidence":0.18837829},{"label":"person","bottomright":{"y":374,"x":280},"topleft":{"y":104,"x":179},"confidence":0.6718636},{"label":"sheep","bottomright":{"y":336,"x":592},"topleft":{"y":145,"x":423},"confidence":0.83751935}]'
            result = str(result).replace("'", '"')
            result = json.loads(result)
            return result, 200
        
        return "AckP", 200
    
    def delete(self):
        return "AckD", 200

class EchoServer(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Fbp', type=list, action='append')
        parser.add_argument('RunOnce', type=bool)
        parser.add_argument('InfiniteLoop', type=bool)
        parser.add_argument('LoopLimit', type=int)
        parser.add_argument('ReturnResult', type=bool)
        args = parser.parse_args()
        
        Fbp = []
        separator = ''
        for i in range(len(args["Fbp"])):
            Fbp.append(separator.join(args["Fbp"][i]))        
        
        result = { 'Fbp': Fbp, 'RunOnce': args['RunOnce'], 'InfiniteLoop': args['InfiniteLoop'], 'LoopLimit': args['LoopLimit'], 'ReturnResult': args['ReturnResult']}
        return result, 200

api.add_resource(TaskServer, '/task')
api.add_resource(EchoServer, '/echo')

app.run(host = "0.0.0.0")
