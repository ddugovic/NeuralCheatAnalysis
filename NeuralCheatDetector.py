#!/usr/bin/python
from pymongo import MongoClient
from pybrain.tools.customxml import NetworkReader
from pybrain.datasets import ClassificationDataSet
import json, cgi

input_text = """[{
	"_id":"oHu556Wx",
	"moveTimes":[20,15,150,40,10,50,60,1,60,100,150,150,10,150,300,300,40,600,300,100,20,300,150,30,150,100,60,50,300,40,80],
	"evals":[15,9,35,29,55,40,38,8,13,-18,-21,-30,-81,-72,-58,-13,332,329,332,398,253,338,277,237,262,309,403,404,352,393,306],
	"diffs":[7,7,0,0,18,0,34,1,50,3,20,44,0,11,5,19,0,90,95,309,74,37,32,0,6,0,0,55,57,67,360],
	"cpAvg":45,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":1682,
	"isProvisional":false
},{	
	"_id":"ZjIoYlul",
	"moveTimes":[80,15,80,30,150,80,80,100,100,40,30,60,40,150,60,60,40,150,150,100,150,15,60,30,30,100,100,30,10,30],
	"evals":[-17,0,5,39,317,304,315,334,615,902,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000],
	"diffs":[3,8,0,0,15,6,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	"cpAvg":2,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":1685,
	"isProvisional":false
},{
	"_id":"9jTdzsKg",
	"moveTimes":[60,30,20,60,50,100,50,40,100,150,100,200,30,300,50,15,600,15,40,100,300,50,40,150,40,20,40,100,300,40,20,30,1,30,80,30,100,80,20,30],
	"evals":[-17,-6,-55,-63,-105,-99,-95,-84,-100,-47,-100,-60,-103,-91,-126,-134,-134,-120,-8,-140,-160,-285,-286,-275,-348,-344,-432,-382,-524,-558,-936,-913,-932,-783,-731,-882,-1000,-1000,-1000,-1000],
	"diffs":[6,42,12,33,0,0,0,38,45,64,0,27,0,57,3,0,0,0,138,18,127,1,0,64,39,98,12,128,138,376,0,42,42,0,126,118,0,0,0,0],
	"cpAvg":44,
	"blurs":0,
	"holdAlert":false,
	"isWinner":false,
	"rating":1679,
	"isProvisional":false
}]"""

# Get posted data
form = cgi.FieldStorage()

input_data = json.loads(form.getvalue("input", input_text))

# Do MongoDB stuff to save data
client = MongoClient()

db = client.tensorFlow
collection = db.gameData

collection.insert(input_data, upsert=true)

print "Content-type: application/json"
print

output = {'decision': json.dumps(input_data), 'cheatPercent': 20}
print json.dumps(output)
