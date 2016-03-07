from pymongo import MongoClient
from paste import request
import json

input_text = """[{
    "_id":"JkxkBnYK",
    "moveTimes":[1,1,5,10,10,10,5,5,10,15,10,5,10,15,20,1,10,10,50,10,15,1,5,1,5,5,1,1,10,10,1,5,10,1,10,1,15,5,20],
    "evals":[-10,-21,-56,-58,-52,-35,-30,-17,-43,31,12,-20,-13,-4,140,-39,75,-6,8,-176,-221,-263,-265,-260,-227,-209,-203,-234,-398,-259,-505,-521,-494,-394,-396,-410,-402,-438,-395],
    "diffs":[29,39,0,12,6,12,0,31,6,68,20,0,0,0,161,0,59,20,191,34,40,4,0,43,16,0,30,150,0,284,17,14,273,6,17,33,37,33,38],
    "cpAvg":44,
    "blurs":0,
    "holdAlert":false,
    "isWinner":true,
    "rating":2460,
    "isProvisional":false
}, {
    "_id":"HGBR2qvo",
    "moveTimes":[20,5,1,5,15,10,10,10,15,10,10,15,1,10,10,10,5,20,10,5,10,10,15,15,10,10,15,30,10,10,10],
    "evals":[15,42,30,33,69,126,131,129,137,121,139,165,90,132,167,256,263,261,248,256,268,278,264,615,733,699,760,805,894,968,1000],
    "diffs":[0,13,9,6,4,0,8,0,43,11,14,121,0,0,120,0,4,17,2,0,30,32,4,7,11,0,0,587,0,403,0],
    "cpAvg":46,
    "blurs":0,
    "holdAlert":false,
    "isWinner":true,
    "rating":2463,
    "isProvisional":false
}, {
    "_id":"COiOop1A",
    "moveTimes":[1,1,10,10,20,20,15,20,15,5,15,10,5,10,1,1,5,1,1,5,20,15],
    "evals":[-20,-17,95,96,158,493,751,755,796,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000],
    "diffs":[10,0,13,0,24,5,10,22,5,123,90,0,0,0,6,0,0,0,0,0,0,0],
    "cpAvg":14,
    "blurs":0,
    "holdAlert":false,
    "isWinner":true,
    "rating":2475,
    "isProvisional":false
}]"""

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/json')])
    analyse(env)
    return [b"Hello World!"]

def analyse(env):
    if (env['REQUEST_METHOD'] == 'POST'):
        fields = request.parse_formvars(env)
        input_data = json.loads(fields.get('input', input_text))
        
        client = MongoClient()
        db = client.tensorFlow
        collection = db.gameData
        collection.insert(input_data)