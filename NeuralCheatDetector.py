#!/usr/bin/python
from pybrain.tools.customxml import NetworkWriter, NetworkReader
from pybrain.datasets import ClassificationDataSet
import json, cgi

#this is just test data, the interface still needs to be finished
input_text = """[{
	"ser":0,
	"aha":0,
	"cmt":0,
	"nfm":1,
	"sha": 0,
	"sfAvg":82,
	"sfSd":130,
	"mtAvg":36,
	"mtSd":34,
	"blurs":0
},
{
	"ser":0,
	"aha":1,
	"cmt":0,
	"nfm":1,
	"sha": 0,
	"sfAvg":32,
	"sfSd":44,
	"mtAvg":45,
	"mtSd":35,
	"blurs":0
},
{
	"ser":0,
	"aha":0,
	"cmt":0,
	"nfm":0,
	"sha": 0,
	"sfAvg":52,
	"sfSd":57,
	"mtAvg":34,
	"mtSd":28,
	"blurs":0
},
{
	"ser":0,
	"aha":0,
	"cmt":0,
	"nfm":1,
	"sha": 0,
	"sfAvg":67,
	"sfSd":168,
	"mtAvg":84,
	"mtSd":82,
	"blurs":0
},
{
	"ser":0,
	"aha":1,
	"cmt":0,
	"nfm":1,
	"sha": 0,
	"sfAvg":45,
	"sfSd":133,
	"mtAvg":57,
	"mtSd":41,
	"blurs":0
}]"""

form = cgi.FieldStorage()

input_data = json.loads(form.getvalue("input", input_text))

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

net_first_pass = NetworkReader.readFrom('FirstPass.xml')

first_pass = ClassificationDataSet(40, 1, nb_classes=2)

temp = sorted(net_first_pass.activateOnDataset(player_assessments), cmp=lambda x, y: cmp(y[1], x[1]))[:20]
temp += [temp[-1]] * (20 - len(temp))
temp = [val for sublist in temp for val in sublist]

first_pass.addSample((
		temp[0],
		temp[1],
		temp[2],
		temp[3],
		temp[4],
		temp[5],
		temp[6],
		temp[7],
		temp[8],
		temp[9],
		temp[10],
		temp[11],
		temp[12],
		temp[13],
		temp[14],
		temp[15],
		temp[16],
		temp[17],
		temp[18],
		temp[19],
		temp[20],
		temp[21],
		temp[22],
		temp[23],
		temp[24],
		temp[25],
		temp[26],
		temp[27],
		temp[28],
		temp[29],
		temp[30],
		temp[31],
		temp[32],
		temp[33],
		temp[34],
		temp[35],
		temp[36],
		temp[37],
		temp[38],
		temp[39]), [1])

net_second_pass = NetworkReader.readFrom('SecondPass.xml')

second_pass = net_second_pass.activateOnDataset(first_pass)

tolerance = 0.7 # 0 = No reports, strictly marking or not marking. 1 = all reports, no marking/non-marking

print "Content-type: text/html"
print

if second_pass[0][0] > second_pass[0][1] - tolerance and second_pass[0][0] < second_pass[0][1] + tolerance:
	print "REPORT"
elif second_pass[0][0] > second_pass[0][1]:
	print "NO-ACTION"
else:
	print "MARK"
