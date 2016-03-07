from pymongo import MongoClient
from paste import request
import json

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/json')])
    addDefinitions(env)
    return [b"Hello World!"]

def addDefinitions(env):
    if (env['REQUEST_METHOD'] == 'POST'):
        fields = request.parse_formvars(env)
        input_data = json.loads(fields.get('input', '[]'))
        
        client = MongoClient()
        db = client.tensorFlow
        collection = db.gameData
        collection.insert(input_data)