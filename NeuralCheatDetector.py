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

# Convert data from JSON to DataSet for processing
player_assessments = ClassificationDataSet(11, 1, nb_classes=2)

for assessment in input_data:
	player_assessments.addSample((
		float(assessment["ser"]),
		float(assessment["aha"]),
		float(assessment["cmt"]),
		float(assessment["nfm"]),
		float(assessment["sha"]),
		float(assessment["sfAvg"]),
		float(assessment["sfSd"]),
		float(assessment["mtAvg"]),
		float(assessment["mtSd"]),
		float(assessment["blurs"]),
		float(assessment["mtSd"] / assessment["mtAvg"])),
		[1])

# Instantiate/Load first neural network
net_first_pass = NetworkReader.readFrom('FirstPass.xml')

# Process and rank games in terms of probability of cheating,
# then pad results with least suspicious result if there are less than 20 games
temp = sorted(net_first_pass.activateOnDataset(player_assessments), cmp=lambda x, y: cmp(y[1], x[1]))[:20]
temp += [temp[-1]] * (20 - len(temp))
temp = [val for sublist in temp for val in sublist] # Flatten list of lists

# Instantiate/Load second neural network
net_second_pass = NetworkReader.readFrom('SecondPass.xml')

# Process results from first neural network
second_pass = net_second_pass.activate(temp)

# Determine what should be done to the player and return results
tolerance = 0.6 # 0 = No reports, strictly marking or not marking. 1 = all reports, no marking/non-marking

print "Content-type: text/html"
print

if second_pass[0] > second_pass[1] - tolerance and second_pass[0] < second_pass[1] + tolerance:
	print "REPORT"
elif second_pass[0] > second_pass[1]:
	print "NO-ACTION"
else:
	print "MARK"
