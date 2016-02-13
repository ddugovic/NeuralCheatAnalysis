#!/usr/bin/python
from pymongo import MongoClient
from pybrain.tools.customxml import NetworkReader
from pybrain.datasets import ClassificationDataSet
import json, cgi

input_text = """[{
	"evals": [-15, -8, -9, -32, -37, -110, -173, -274, -610, -720, -690, -957, -719, -702, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000],
	"diffs": [2, 8, 0, 27, 3, 43, 19, 107, 0, 91, 3, 256, 26, 0, 0, 0, 15, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	"moveTimes": [5, 1, 1, 1, 1, 1, 10, 1, 10, 1, 5, 5, 5, 10, 15, 5, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	"holdAlert": false,
	"isProvisional": false,
	"rating": 2448,
	"isWinner": true, 
	"blurs": 0, 
	"cpAvg": 17
}]"""

# Get posted data
form = cgi.FieldStorage()

input_data = json.loads(form.getvalue("input", input_text))

# Do MongoDB stuff to save data
client = MongoClient()

db = client.tensorFlow
collection = db.gameData

collection.insert_many(input_data)

print "Content-type: application/json"
print

output = {'decision': json.dumps(input_data), 'cheatPercent': 20}
print json.dumps(output)
