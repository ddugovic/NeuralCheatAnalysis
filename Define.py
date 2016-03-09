from pymongo import MongoClient
from paste import request
import json

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/json')])
    return define(env).encode('UTF-8')

def define(env):
    if (env['REQUEST_METHOD'] == 'POST'):
        fields = request.parse_formvars(env)
        input_data = json.loads(fields.get('input', '[]'))
        
        client = MongoClient()
        db = client.tensorFlow
        collection = db.gameData
        collection.insert(input_data)
        return json.dumps({"nbAdded": len(input_data)})
    else:
        return json.dumps({"nbAdded": 0})