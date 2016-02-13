#!/usr/bin/python
from pymongo import MongoClient
from pybrain.tools.customxml import NetworkReader
from pybrain.datasets import ClassificationDataSet
import json, cgi

input_text = ""

# Get posted data
form = cgi.FieldStorage()

input_data = json.loads(form.getvalue("input", input_text))

# Do MongoDB stuff to save data
client = MongoClient()

db = client.tensorFlow
collection = db.gameData

collection.insert(input_data)

print "Content-type: application/json"
print

output = {'decision': json.dumps(input_data), 'cheatPercent': 20}
print json.dumps(output)
