from pymongo import MongoClient
from paste import request
import json

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/json')])
    return analyse(env)

def analyse(env):
    if (env['REQUEST_METHOD'] == 'POST'):
        fields = request.parse_formvars(env)
        input_data = json.loads(fields.get('input', '[]'))
        
        # I dunno lol
        return json.dumps({"decision": "REPORT", "cheatPercent": len(input_data)})
    elif:
        return json.dumps({"decision": "NO-ACTION", "cheatPercent": 0})