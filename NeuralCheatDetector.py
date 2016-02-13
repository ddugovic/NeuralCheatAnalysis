#from pymongo import MongoClient
from pybrain.tools.customxml import NetworkReader
from pybrain.datasets import ClassificationDataSet
import json, cgi, sys

input_text = """[{
	"_id":"VxrF4mh9",
	"moveTimes":[5,1,1,1,1,1,10,1,10,1,5,5,5,10,15,5,10,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	"evals":[15,8,9,32,37,110,173,274,610,720,690,957,719,702,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000],
	"diffs":[2,8,0,27,3,43,19,107,0,91,3,256,26,0,0,0,15,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	"cpAvg":17,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2448,
	"isProvisional":false
}, {
	"_id":"Za8hH5nF",
	"moveTimes":[5,1,5,5,5,5,1,1,1,1,5,5,5,10,10,5,10,5,5,10,10,1,10,5,10,5,5,15,5,1,5,5,10,20,10,10,1,1,5,5,5,1,5,15],
	"evals":[15,18,13,22,72,38,25,35,30,45,204,239,236,137,167,86,78,45,68,94,94,131,155,153,161,158,185,148,90,80,86,98,221,365,248,231,715,686,830,891,1000,1000,1000,1000],
	"diffs":[2,2,2,18,31,17,0,0,0,15,157,0,96,0,90,23,34,68,0,7,7,1,9,1,6,0,33,35,8,0,0,35,0,135,11,0,49,0,55,60,31,0,0,0],
	"cpAvg":23,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2448,
	"isProvisional":false
}, {
	"_id":"p1QPXzmA",
	"moveTimes":[10,1,1,1,5,1,1,10,5,1,5,5,5,30,20,10,10,10,15,15,15,10,15,15,1,1,1,1,1,1,5,10,1,10,1,20,10,15],
	"evals":[15,13,12,7,94,73,71,139,55,25,30,27,51,10,189,160,164,78,77,110,96,93,100,174,125,144,96,153,225,260,665,468,129,494,1000,539,577,527],
	"diffs":[4,6,2,4,77,34,36,95,29,0,5,3,20,10,86,0,85,0,0,31,5,52,16,81,8,44,0,64,89,5,547,341,45,5,535,9,131,0],
	"cpAvg":65,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2403,
	"isProvisional":false
}]"""

# Get posted data
form = cgi.FieldStorage()

input_data = json.loads(form.getvalue("input", input_text))

# Do MongoDB stuff to save data
#client = MongoClient()

#db = client.tensorFlow
#collection = db.gameData

#collection.insert(input_data)

print "Content-type: application/json"
print

output = {'decision': sys.version_info, 'cheatPercent': 20}
#output = {'decision': json.dumps(input_data), 'cheatPercent': 20}
print json.dumps(output)
