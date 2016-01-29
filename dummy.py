#!/usr/bin/python
from pybrain.tools.customxml import NetworkReader
from pybrain.datasets import ClassificationDataSet
import json, cgi

input_text = """[{
	"ser":0,
	"aha":0,
	"cmt":0,
	"nfm":0,
	"sha": 0,
	"sfAvg":82,
	"sfSd":130,
	"mtAvg":46,
	"mtSd":34,
	"blurs":0
}]"""

# Get posted data
form = cgi.FieldStorage()

input_data = json.loads(form.getvalue("input", input_text))

target = open("dummy.txt", 'w')
target.write(input_data)

print "Content-type: application/json"
print

output = {'decision': decision, 'cheatPercent': int(10), 'nonCheatPercent': int(90)}
print json.dumps(output)