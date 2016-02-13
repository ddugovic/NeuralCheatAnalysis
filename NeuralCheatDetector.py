#!/usr/bin/python
#from pymongo import MongoClient
from pybrain.tools.customxml import NetworkReader
from pybrain.datasets import ClassificationDataSet
import json, cgi

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
}, {
	"_id":"golhADx9",
	"moveTimes":[1,10,5,10,5,1,1,1,10,1,1,5,10,1,5,1,1,5,1,5,10,15,15,5,15,1,10,10,10,1,1,1,15,1,10,1,10,10,1,1,5,1,1,1,1,1,5,1],
	"evals":[-10,-15,27,10,12,0,34,21,62,65,13,20,439,470,451,492,521,585,559,632,615,767,849,628,652,705,875,1000,1000,1000,1000,1000,1000,1000,1000,1000,608,641,645,637,643,552,541,573,506,582,546,624],
	"diffs":[40,14,6,3,9,1,9,5,0,53,0,8,0,31,0,46,13,16,0,20,10,208,317,87,11,31,11,93,0,0,0,170,0,0,0,382,3,0,0,0,88,29,0,0,0,51,0,624],
	"cpAvg":49,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2404,
	"isProvisional":false
}, {
	"_id":"3cEaMcpl",
	"moveTimes":[15,1,5,10,1,1,10,5,1,1,5,5,5,5,10,15,1,60,15,15],
	"evals":[15,60,23,28,18,3,23,22,24,22,14,52,101,58,18,2,134,93,24,-140],
	"diffs":[0,91,8,9,13,0,0,6,0,27,4,69,125,48,10,0,37,318,169,860],
	"cpAvg":89,
	"blurs":0,
	"holdAlert":false,
	"isWinner":false,
	"rating":2295,
	"isProvisional":false
}, {
	"_id":"dc15k1rt",
	"moveTimes":[5,1,1,1,1,10,10,1,5,5,10,1,15,1,10,5,20,20,10,10,10,15,5,15,5,10,10,5,1,10,5,1,10],
	"evals":[-19,-23,-46,-41,-56,-26,-17,-43,-48,-47,-54,-48,-1,-16,25,24,248,125,106,106,155,222,301,486,808,1000,1000,1000,1000,1000,1000,1000,1000],
	"diffs":[5,36,6,15,0,31,30,19,15,13,8,11,0,0,0,11,143,15,38,6,24,51,0,20,34,188,166,0,0,0,100,0,0],
	"cpAvg":29,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2235,
	"isProvisional":false
}, {
	"_id":"dbKnvaaa",
	"moveTimes":[1,1,5,5,10,5,10,1,1,10,5,1,10,5,1,10,15,10,5,1,20,5,5,5,20,5,10,100,1,1,5,1,10,15,1,1,10,1],
	"evals":[-10,-17,-16,-13,-35,36,13,18,15,32,35,8,82,27,22,21,16,22,44,-9,0,20,35,0,-40,21,-2,-144,-531,0,0,28,970,821,1000,1000,573,1000],
	"diffs":[33,40,12,41,85,30,1,4,15,58,46,39,64,7,82,13,5,0,44,0,48,5,31,0,12,5,214,361,469,0,0,0,949,146,0,990,584,836],
	"cpAvg":138,
	"blurs":0,
	"holdAlert":false,
	"isWinner":false,
	"rating":2326,
	"isProvisional":false
}, {
	"_id":"I4c1sWVA",
	"moveTimes":[5,1,1,5,5,1,1,1,5,1,5,5,1,1,1,10,10,5,1,1,1,1,5,1,1,1,5,1,1,1,1],
	"evals":[15,55,30,-39,-36,-317,-327,-317,-295,-324,-325,-352,-356,-338,-436,-431,-393,-402,-315,-404,-413,-422,-434,-361,-486,-468,-508,-588,-581,-637,-685],
	"diffs":[0,42,69,8,290,13,0,2,30,1,25,17,4,107,98,63,69,61,101,9,48,8,14,209,7,35,86,28,51,82,315],
	"cpAvg":61,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2333,
	"isProvisional":false
}, {
	"_id":"OMr9TU9U",
	"moveTimes":[1,1,1,1,5,1,1,1,1,1,1,1,5,5,5,10,5,15,1,10,10,5,10,1,15,1,1,1,1,1,1,1,1],
	"evals":[15,23,10,2,54,43,-8,-32,-15,-73,-39,-34,-58,-46,-75,-34,-36,6,0,238,252,294,290,317,329,272,44,15,-272,-412,-1000,-1000,-1000],
	"diffs":[28,16,5,1,20,73,10,23,45,0,16,34,21,33,0,131,5,14,38,267,343,82,0,7,224,229,26,259,133,588,0,0,0],
	"cpAvg":80,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2295,
	"isProvisional":false
}, {
	"_id":"pbk0MQrX",
	"moveTimes":[10,1,1,1,1,1,5,10,5,15,5,5,1,1,10,10,30,10,5,10,15,5,10,20,5,15,5,10,1,5],
	"evals":[15,6,14,28,31,-3,0,8,35,65,47,47,67,56,65,39,-29,-5,-81,-104,-221,-117,-481,-450,-816,-235,-289,-306,-282,-1000],
	"diffs":[20,2,0,0,31,27,2,119,0,5,0,14,0,0,29,121,8,87,19,113,211,338,0,284,86,327,28,34,718,0],
	"cpAvg":87,
	"blurs":0,
	"holdAlert":false,
	"isWinner":false,
	"rating":2324,
	"isProvisional":false
}, {
	"_id":"7nWLRbTM",
	"moveTimes":[1,1,5,5,5,5,5,30,5,5,5,5,10,15,5,5,5,5,5,15,5,10,10,15,10,5,1,5,5,10,1,1],
	"evals":[-22,-15,-13,-567,-214,-143,490,0,6,120,105,144,216,168,188,200,144,136,232,962,603,638,431,266,354,326,374,495,605,408,389,393],
	"diffs":[28,38,561,0,3,18,537,61,7,0,2,6,115,101,6,50,72,0,0,491,144,324,166,11,22,6,10,136,251,5,57,0],
	"cpAvg":100,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2304,
	"isProvisional":false
}, {
	"_id":"vTixnIiw",
	"moveTimes":[5,5,5,10,5,5,5,5,5,5,15,10,5,5,15,15,15,10,15],
	"evals":[15,6,8,55,54,71,86,68,66,67,177,744,785,706,1000,1000,1000,1000],
	"diffs":[26,0,14,11,9,0,16,41,7,67,223,515,362,0,288,0,0,0],
	"cpAvg":87,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2311,
	"isProvisional":false
}, {
	"_id":"0vwGlXVY",
	"moveTimes":[5,1,1,5,15,5,5,5,10,1,1,10,10,1,5,1,15,15,1,5,15,5,10,10,10,10,1,5,5,5,5,5,10,1],
	"evals":[15,-7,-8,0,-18,-11,13,6,-10,-11,-15,-23,-17,0,0,-15,-10,15,-20,-7,63,61,70,135,1000,1000,814,842,831,919,1000,1000,1000,1000],
	"diffs":[23,0,0,20,0,4,52,37,0,3,13,0,10,9,15,4,14,38,0,1,0,56,0,132,0,184,63,12,0,0,0,0,0,0],
	"cpAvg":20,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2315,
	"isProvisional":false
}, {
	"_id":"k6AgfVTa",
	"moveTimes":[1,10,5,5,5,1,5,10,5,5,20,10,10,10,5,5,15,5,20,5,1,5,10,15,1,1,10,1,1,1,1,1,5],
	"evals":[-13,-33,10,19,17,16,31,74,85,69,90,40,210,31,63,92,109,88,97,4,350,108,394,1000,1000,1000,1000,1000,1000,1000,1000,1000],
	"diffs":[48,1,0,0,2,9,0,0,60,0,40,0,196,16,20,93,14,88,85,68,255,4,0,0,0,0,0,0,0,0,0,0],
	"cpAvg":31,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2309,
	"isProvisional":false
}, {
	"_id":"4MNS4Ty4",
	"moveTimes":[5,1,1,5,10,5,5,1,1,1,5,15,10,15,5,5,10,5,5,1,5,5,5,5,5,10,5,1,1,5,5,5,5,5,5,15],
	"evals":[15,4,10,-45,-27,-24,30,29,-13,-22,-13,-9,7,311,326,331,494,527,531,473,467,469,467,469,468,479,489,531,572,544,520,941,1000,1000,1000],
	"diffs":[30,0,76,0,13,1,10,41,13,19,24,4,7,1,10,15,1,0,43,58,0,1,2,1,0,0,0,18,51,38,23,316,0,0,0],
	"cpAvg":23,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2310,
	"isProvisional":false
}, {
	"_id":"qFaK9TwL",
	"moveTimes":[15,10,10,5,10,5,10,1,10,1,5,10,5,5,5,15,5,10,10,15,10,10,5,10],
	"evals":[15,24,15,43,34,0,-1,-31,-1,0,0,86,249,245,296,526,643,698,801,1000,1000,1000,1000],
	"diffs":[0,41,15,22,39,28,93,8,24,0,0,15,31,0,84,0,14,0,77,0,0,0,0],
	"cpAvg":21,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2293,
	"isProvisional":false
}, {
	"_id":"4H468nH9",
	"moveTimes":[5,5,1,5,10,5,5,5,5,5,5,5,5,10,5,15,1,10,10,15,1,30,1,15,1,20,15,1,10,15,10],
	"evals":[15,22,-18,-16,-13,-72,-71,-61,-87,-75,-71,-52,-10,167,88,532,528,472,0,-62,-181,-124,-194,-177,-184,-303,-312,-389,-435,-294],
	"diffs":[4,41,0,14,64,0,4,22,36,16,2,7,21,143,10,0,360,435,58,117,0,60,0,9,453,26,85,414,428,18],
	"cpAvg":94,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2295,
	"isProvisional":false
}, {
	"_id":"7nA9Lumz",
	"moveTimes":[80,40,30,60,20,150,40,10,40,40,30,100,100,100,200,100,30,150,150,20,5,30,50,40,60,60,30,20,30,20,100,60,20,80,1,80,80,60,15,30,15],
	"evals":[-11,-72,-69,-68,-62,-48,-51,-50,0,0,0,12,22,5,0,23,28,12,15,9,0,16,5,0,0,45,79,67,143,161,173,167,137,257,244,317,577,417,758,1000],
	"diffs":[56,0,0,4,6,17,0,1,0,0,0,0,3,5,6,62,28,17,5,1,0,16,5,0,0,17,14,2,4,0,0,28,0,0,0,0,189,142,465,0],
	"cpAvg":27,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2327,
	"isProvisional":false
}, {
	"_id":"n6BdeomO",
	"moveTimes":[30,30,60,400,200,10,300,30,20,30,100,200,80,10,60,150,20,80,150,50,5,20,15,10,15,5],
	"evals":[-10,-6,-4,15,0,0,19,21,32,57,60,60,46,-39,-32,50,87,92,101,130,140,140,136,192,343,419],
	"diffs":[0,1,1,21,12,24,18,3,19,25,43,12,73,0,28,7,3,0,13,10,2,36,0,2,2,90],
	"cpAvg":17,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2321,
	"isProvisional":false
}, {
	"_id":"RBhPbE3C",
	"moveTimes":[10,5,10,10,15,5,5,5,5,5,5,1,5,10,5,20,1,5,5,10,15,15,30,5,15,10,20,10,15,10,20],
	"evals":[-31,-20,-15,-11,-12,-8,1,-4,-2,-15,-6,-12,-13,32,34,257,256,253,270,385,386,391,420,460,527,562,620,633,906,889,1000],
	"diffs":[0,9,0,0,3,2,16,1,9,4,36,0,0,7,34,0,0,0,0,40,0,0,2,0,24,0,22,8,0,30,105],
	"cpAvg":11,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2346,
	"isProvisional":false
}, {
	"_id":"c7Aou46r",
	"moveTimes":[10,5,5,5,5,5,5,15,15,15,10,1,30,5,10,5,20,5,15,10,10,15,15,10,10,30,20],
	"evals":[-8,7,-35,-21,-20,-32,-11,-3,1,-4,0,-19,13,-58,44,36,8,56,56,53,58,52,256,320,382,872],
	"diffs":[14,20,0,8,13,23,1,5,14,8,29,5,36,0,10,38,8,60,0,0,9,6,1,27,20,293],
	"cpAvg":24,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2354,
	"isProvisional":false
}, {
	"_id":"bzZPDXZz",
	"moveTimes":[20,1,10,1,5,5,5,10,20,30,30,5,1,1,5,1,20,5,15,20,15,10,5,10,5,10,10,1,1,10,10,15,10,5,10,5,1,15,1,1,5,1,5],
	"evals":[15,3,21,3,0,22,-6,0,0,-43,-44,-56,75,85,118,95,236,246,296,562,240,334,261,196,195,199,212,173,155,231,272,478,562,963,914,991,1000,1000,1000,1000,1000,1000],
	"diffs":[25,0,11,15,9,38,11,18,47,4,19,0,63,16,42,11,0,30,18,382,0,91,70,15,3,51,22,12,43,4,0,0,17,290,284,7,54,0,0,0,0,0],
	"cpAvg":41,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2378,
	"isProvisional":false
}, {
	"_id":"PXdyX5MH",
	"moveTimes":[20,10,10,10,10,10,5,5,5,5,10,5,5,10,10,5,1,10,10,5,20,30,10,20,80,10,1,5,15,10,5,30,5,10,5,5,5,30,10],
	"evals":[15,42,59,58,60,85,79,78,80,94,112,105,91,98,84,58,62,48,25,39,115,123,270,200,-161,-354,-598,-636,-562,-812,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
	"diffs":[0,4,0,0,0,4,0,1,0,10,0,4,0,8,31,3,8,15,0,12,0,17,62,384,196,259,0,0,237,188,0,0,0,0,0,0,0,0,0],
	"cpAvg":37,
	"blurs":0,
	"holdAlert":false,
	"isWinner":false,
	"rating":2405,
	"isProvisional":false
}, {
	"_id":"sLpgAzkK",
	"moveTimes":[20,5,5,10,5,5,10,5,1,1,5,5,10,5,1,5,10,20,20,20,50,1,1,5,10,15,5,10,5,1,1,1,5,5,10,5,1,20,15,50,10,5,1,20],
	"evals":[15,56,32,39,-47,-52,189,232,215,217,181,252,146,125,152,184,168,45,55,58,92,-257,-260,-271,-337,-293,-272,-298,-203,-250,-212,-196,-922,-944,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
	"diffs":[0,49,10,80,0,3,23,20,35,25,0,87,5,0,25,13,129,15,192,0,350,0,0,62,0,13,15,0,55,8,38,740,36,56,0,0,0,0,0,0,0,0,0,0],
	"cpAvg":47,
	"blurs":0,
	"holdAlert":false,
	"isWinner":false,
	"rating":2387,
	"isProvisional":false
}, {
	"_id":"jH7FXipH",
	"moveTimes":[20,10,5,5,10,15,10,10,5,10,20,10,5,30,30,5,10,10,10,1,10,15,20,10,5,1,5,5,10,5],
	"evals":[15,13,20,106,104,73,26,3,5,-6,40,43,73,492,863,684,688,700,1000,688,796,1000,770,772,775,1000,1000,1000,1000],
	"diffs":[0,1,12,19,17,45,29,0,10,2,0,1,5,0,181,15,0,24,310,19,112,430,0,4,1,0,0,0,0],
	"cpAvg":42,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2396,
	"isProvisional":false
}, {
	"_id":"6jmnjoVL",
	"moveTimes":[1,1,5,1,1,1,1,5,5,5,10,1,10,5,5,5,5,10,10,10,10,1,10,5,5,15,15,10,20,10,1,5,1,1,10,1,5,1,10],
	"evals":[-23,-25,-39,-15,-17,-37,1,-14,-6,-20,105,112,113,118,113,112,112,91,125,100,92,0,-8,55,130,127,133,532,112,162,19,325,300,117,318,1000,579,563,594],
	"diffs":[10,4,2,6,43,0,14,11,30,0,0,4,1,8,7,60,23,13,35,38,142,0,0,2,3,0,2,493,45,114,0,68,171,0,177,607,111,0,0],
	"cpAvg":57,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2423,
	"isProvisional":false
}, {
	"_id":"5FQVN1CW",
	"moveTimes":[5,1,1,5,5,5,5,5,10,10,5,1,5,5,10,15,10,10,10,5,10,10,5,10],
	"evals":[15,24,17,25,10,-9,-40,-43,-46,-32,-37,-28,-13,5,25,-5,-6,-19,-27,-11,70,132,147,337],
	"diffs":[0,9,22,30,5,35,8,10,12,1,15,0,0,30,39,13,20,12,11,0,8,0,0,0],
	"cpAvg":11,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2426,
	"isProvisional":false
}, {
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
}, {
	"_id":"OlvhNe3P",
	"moveTimes":[40,1,5,10,1,5,5,5,10,20,10,20,15,5,30,60,50,1,5,20,5,10,5,15],
	"evals":[15,48,55,54,148,18,0,3,8,-15,-15,32,49,-33,-31,0,0,-179,-135,-286,-295,-171,-120,-63],
	"diffs":[0,30,5,6,124,0,0,7,21,35,4,22,90,0,0,0,171,0,150,6,11,177,139,92],
	"cpAvg":45,
	"blurs":0,
	"holdAlert":false,
	"isWinner":false,
	"rating":2483,
	"isProvisional":false
}, {
	"_id":"JDH4KklX",
	"moveTimes":[10,5,1,5,5,1,5,5,5,10,1,1,5,1,15,5,5,1,20,5,1,5,1,5],
	"evals":[5,-8,23,51,46,26,267,280,298,793,789,785,779,843,787,828,915,924,1000,1000,1000,1000,1000],
	"diffs":[11,2,17,0,22,2,3,9,65,0,0,12,89,104,0,27,1,0,0,0,0,0,0],
	"cpAvg":15,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2464,
	"isProvisional":false
}, {
	"_id":"oqnJzvTa",
	"moveTimes":[10,10,1,1,5,5,5,10,15,30,1,10,15,10,10,30,10,15,20,15,10,10,10,5,1,10,5,5,5,5,5,10,10,5,5,10,5,1],
	"evals":[-21,-25,-28,-15,-22,-20,-17,10,13,124,-33,-34,-4,-7,-54,-69,-48,-26,-23,-13,-14,-22,-10,-11,-55,-25,-38,-17,-17,-17,-26,-13,-101,-157,-178,-105,-110,-59],
	"diffs":[24,0,3,0,9,2,4,13,12,159,3,18,8,41,2,14,28,20,0,5,5,60,0,51,8,7,0,5,9,38,55,81,74,33,25,10,0,0],
	"cpAvg":21,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2485,
	"isProvisional":false
}, {
	"_id":"4vbbN6Uk",
	"moveTimes":[20,1,1,1,5,5,10,5,5,1,5,5,10,5,5,5,5,20,20,20,15,30,1,10,10,1,1,1,20,15,15,10,10,20,20,30,20,30,10],
	"evals":[15,48,44,41,43,31,12,0,28,27,46,12,24,0,0,13,34,49,72,90,221,318,266,254,265,263,225,215,236,270,292,265,284,1000,298,282,542,838],
	"diffs":[0,12,7,13,13,16,22,0,12,5,46,23,34,12,6,0,2,3,0,90,173,0,2,0,62,47,3,52,0,7,62,20,0,702,31,7,244,41],
	"cpAvg":46,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2529,
	"isProvisional":false
}, {
	"_id":"W5xlncyU",
	"moveTimes":[20,5,5,10,1,10,5,15,10,5,5,15,10,10,10,10,30,1,15,10,5,20,5,1,15,10,1,15,10,15,5,10,10,15,15,5,10,10,1,10,1,15,10,5,30,10,1],
	"evals":[15,20,37,11,-5,-6,498,-20,338,4,6,44,37,7,19,25,32,23,24,36,34,22,5,41,10,14,17,228,27,48,50,46,54,154,56,48,55,165,51,468,507,615,885,1000,1000,1000,1000],
	"diffs":[0,4,27,8,0,0,539,0,339,0,6,35,29,2,10,8,9,0,0,12,21,12,0,31,0,8,6,197,0,1,11,19,3,105,0,0,0,122,51,41,22,116,0,0,0,0,0],
	"cpAvg":38,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2531,
	"isProvisional":false
}, {
	"_id":"yeDU3ZOI",
	"moveTimes":[30,1,5,5,5,5,1,5,1,5,5,1,5,1,10,5,5,10,10,10,5,20,10,15,30,10,20,60,30],
	"evals":[15,8,9,6,248,232,248,-13,-382,-384,-319,-287,-362,-378,-366,-373,-355,-368,-381,-371,-427,-450,-426,-422,-566,-688,-553,-1000,-1000],
	"diffs":[33,3,3,0,198,9,256,371,0,22,0,66,18,0,7,13,10,8,36,56,49,12,10,195,151,17,447,0,0],
	"cpAvg":68,
	"blurs":0,
	"holdAlert":false,
	"isWinner":false,
	"rating":2551,
	"isProvisional":false
}, {
	"_id":"pbODDpUf",
	"moveTimes":[30,5,5,1,1,1,1,1,10,1,5,1,15,5,5,15,20,5,10,10,5,20,10,20,15,15,10,10,10,10,10,10,10,5,1,15,5,5,1,10,10,10,30,10,1],
	"evals":[15,8,28,26,32,1,9,13,15,14,32,20,4,152,51,71,180,193,431,435,497,421,451,485,638,413,513,626,625,580,962,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000],
	"diffs":[28,1,1,18,32,2,1,13,0,0,27,19,4,131,14,16,7,0,0,2,85,0,6,71,193,0,51,0,13,0,30,0,0,0,0,0,0,0,0,0,0,0,0,0],
	"cpAvg":17,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2519,
	"isProvisional":false
}, {
	"_id":"qFOSVKsx",
	"moveTimes":[10,5,5,5,5,10,5,10,10,5,10,10,1,15,20,5,1,30,30,15,1,10,20],
	"evals":[-12,-21,5,-3,1,10,7,1,5,7,2,-28,-208,-236,102,-158,280,681,596,1000,1000,1000,1000],
	"diffs":[8,0,17,11,7,10,7,81,4,5,235,180,46,81,246,17,0,122,371,0,0,0,0],
	"cpAvg":62,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2521,
	"isProvisional":false
}, {
	"_id":"dPcZwSPn",
	"moveTimes":[20,1,1,5,5,10,10,5,5,20,15,10,10,10,10,5,10,10,10,20,20,5,10,5,10],
	"evals":[15,7,5,7,10,9,3,5,-3,27,67,87,120,206,310,294,378,394,385,412,384,414,577,585,1000],
	"diffs":[38,7,0,1,1,2,0,2,0,13,0,28,69,159,15,5,31,63,0,35,0,70,230,280,19],
	"cpAvg":42,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2523,
	"isProvisional":false
}, {
	"_id":"K3vgHm4Z",
	"moveTimes":[10,1,1,5,15,10,15,10,10,5,10,10,10,1,15,10,10,15,1,10,1,15,1,10,20],
	"evals":[-12,-14,-10,50,31,12,4,9,40,17,-18,-4,29,36,-22,-45,1,127,123,127,114,316,341,368,1000],
	"diffs":[22,0,1,51,6,15,4,0,65,29,0,1,0,90,14,0,0,0,16,32,8,0,31,10,0],
	"cpAvg":15,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2526,
	"isProvisional":false
}, {
	"_id":"9cd1tZkb",
	"moveTimes":[30,1,5,5,10,10,15,5,10,5,5,5,10,5,5,15,1,10,15,5,15,20,10,10,15,20,20,40,15,20,5,15,20,20,10,15,5,15,10],
	"evals":[15,18,20,29,39,69,70,93,61,63,51,67,64,-29,6,4,11,241,263,289,231,227,186,182,241,246,421,321,316,493,542,521,744,934,1000,1000,1000,1000,1000],
	"diffs":[19,17,20,0,0,4,2,34,0,15,0,1,101,2,0,2,34,3,1,53,14,53,7,324,0,8,210,0,421,0,311,340,31,19,0,0,0,0,0],
	"cpAvg":52,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2561,
	"isProvisional":false
}, {
	"_id":"mcyPL8fd",
	"moveTimes":[5,10,1,5,5,20,5,15,20,10,10,1,10,15,15,10,15,10,10,30,80,1,15,15,20,10,30,1,5,20,15,15],
	"evals":[-9,-27,-17,-15,-36,-50,-50,-39,-62,-25,-54,-51,-7,-27,-27,-67,-82,-96,-55,56,-70,-75,-86,-86,-89,-123,-23,-203,-112,-72,644],
	"diffs":[14,0,0,28,7,0,0,23,8,29,0,0,54,50,54,34,18,2,46,146,21,19,9,9,55,7,173,0,0,0,0],
	"cpAvg":26,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2574,
	"isProvisional":false
}, {
	"_id":"zL0dogsZ",
	"moveTimes":[30,10,15,10,15,10,5,15,20,10,10,10,10,1,30,15,10,15,10,15],
	"evals":[15,36,61,6,72,87,79,79,127,45,141,354,587,334,377,480,536,592,631,637],
	"diffs":[0,1,54,16,8,20,3,2,83,6,7,0,249,31,26,11,0,0,7,9],
	"cpAvg":26,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2576,
	"isProvisional":false
}, {
	"_id":"tacLGe1f",
	"moveTimes":[10,1,10,5,5,10,10,5,5,10,15,10,10,15,15,10,10,20,5,5,5,10,15,10,5,30,10,50,5,10,5,10,30,15,10,20,10,15],
	"evals":[-13,-56,-58,-62,-67,-44,-45,-44,-24,-23,-11,0,-8,-34,39,-24,-62,-103,-100,-112,-102,-112,4,-22,-19,10,2,18,17,42,144,582,557,196,620,665,687,1000],
	"diffs":[52,0,8,1,7,7,0,0,0,0,39,6,28,29,97,25,30,19,17,0,10,5,120,0,0,3,2,18,8,0,22,235,396,33,0,0,177,313],
	"cpAvg":44,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2593,
	"isProvisional":false
}, {
	"_id":"pDfIYUxu",
	"moveTimes":[30,10,5,10,20,15,5,30,20,15,15,15,20,10,50,20,30,10,15,20,10,10,5,10,10,5,5,10,10,1,10,30,10,15,15,15],
	"evals":[15,57,48,27,45,72,21,221,-32,22,0,-29,-105,-100,-53,-60,-66,-85,18,19,-16,63,278,158,197,468,1000,1000,1000,848,1000,1000,1000,1000,1000],
	"diffs":[4,16,22,0,30,60,0,258,2,19,42,64,0,344,0,15,9,20,170,19,22,0,121,0,8,0,0,0,204,0,0,23,0,0,0],
	"cpAvg":42,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2595,
	"isProvisional":false
}, {
	"_id":"FrnIdUDW",
	"moveTimes":[30,10,15,10,20,20,5,15,20,10,10,5,15,10,15,10,30,20,10],
	"evals":[15,41,23,32,40,44,13,31,44,-31,9,148,461,117,745,747,1000,1000],
	"diffs":[0,17,7,0,43,38,11,8,69,0,0,98,353,0,18,0,0,0],
	"cpAvg":36,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2613,
	"isProvisional":false
}, {
	"_id":"OBNXn6j8",
	"moveTimes":[40,5,5,10,20,10,5,20,10,15,15,10,10,1,15,30,15,15,20,10,15,15,10,1,5,20,30,20,50,30,10,15,5,10,10],
	"evals":[15,28,-2,0,-6,-49,-40,-48,-40,-37,-74,-79,-10,-15,31,62,195,41,68,31,41,51,193,179,176,525,501,394,393,428,796,378,375,369,458],
	"diffs":[0,36,0,0,26,1,4,22,0,111,24,0,38,23,0,2,164,2,48,31,4,40,6,0,0,32,89,0,28,41,422,39,0,0,5],
	"cpAvg":35,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2613,
	"isProvisional":false
}, {
	"_id":"FanopkDO",
	"moveTimes":[5,1,10,10,10,5,20,80,15,20,5,10,10,10,10,15,15,5,5,15,15,15,30,5,5,1,10,30,30,20,20,20,15,10,15,5,5,10,10,10,15,15,10,1,5,5],
	"evals":[-25,-51,50,29,29,48,44,95,136,96,90,102,93,131,122,67,9,16,14,466,466,474,634,632,645,617,660,560,608,628,671,655,687,630,629,572,557,656,809,830,884,1000,1000,1000,1000],
	"diffs":[25,0,11,4,0,17,10,0,75,10,1,35,26,0,60,51,0,5,0,5,3,0,0,22,20,66,166,2,41,0,40,0,90,1,65,0,0,52,45,0,0,0,0,0,0],
	"cpAvg":21,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2613,
	"isProvisional":false
}, {
	"_id":"5X8h1OMS",
	"moveTimes":[20,5,5,10,5,5,5,15,5,15,20,10,10,20,10,10,1,50,30,5,10,10,5,10,10,10,5,5],
	"evals":[15,58,62,51,48,49,65,58,56,53,47,75,30,31,39,58,77,74,6,0,60,93,67,5,20,361,425,1000],
	"diffs":[3,27,25,0,0,0,39,7,11,1,0,32,0,0,9,0,0,74,6,0,12,15,67,2,56,0,21,0],
	"cpAvg":14,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2619,
	"isProvisional":false
}, {
	"_id":"EeXL0IRT",
	"moveTimes":[30,15,10,5,5,15,5,10,5,5,10,5,10,15,10,10,30,10,20,20,15,10,5,1,60,20,10,10,10,15,10,1,10,15,10],
	"evals":[15,47,53,63,55,42,38,27,22,53,171,171,165,250,350,474,434,502,502,666,777,803,925,319,315,293,361,381,466,777,802,582,558,713,677],
	"diffs":[1,0,6,4,11,3,19,8,0,39,0,0,20,14,0,33,62,0,105,13,7,0,608,0,16,4,24,69,0,0,242,0,0,48,11],
	"cpAvg":39,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2622,
	"isProvisional":false
}, {
	"_id":"KsJHYND7",
	"moveTimes":[20,5,1,1,10,10,20,10,10,10,10,15,10,10,5,10,1,20,15,15,15,5],
	"evals":[15,31,110,76,0,-10,-41,-50,-27,-8,18,64,122,604,772,664,779,676,1000,1000,1000],
	"diffs":[0,22,28,76,15,62,16,39,10,0,29,0,52,334,131,14,132,121,0,0,0],
	"cpAvg":51,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2623,
	"isProvisional":false
}, {
	"_id":"ebyVmI1d",
	"moveTimes":[30,10,5,5,10,10,10,10,5,5,10,15,5,15,10,10,15,10,15,1,20,15,15],
	"evals":[15,48,15,60,87,95,86,72,62,72,78,98,144,153,281,214,764,700,844,839,951,1000,1000],
	"diffs":[0,29,0,13,1,1,11,36,0,28,30,0,6,0,84,0,553,7,67,102,208,0,0],
	"cpAvg":51,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2644,
	"isProvisional":false
}, {
	"_id":"Z0RqW6Ul",
	"moveTimes":[30,5,5,20,5,5,15,30,20,60,5,15,15,50,15,10,50,30,10,10,20,20,15,15,20,10,15,5,1,1,10,1,10,1,1,5],
	"evals":[15,48,48,50,45,39,49,13,-51,-20,-110,-87,-137,-79,-59,27,112,17,72,71,137,122,252,1000,259,246,339,270,188,247,324,279,323,284,305,436],
	"diffs":[0,2,4,16,1,0,45,63,0,92,90,49,76,9,1,14,107,4,60,6,165,12,96,738,15,0,63,74,0,125,28,74,28,0,0,52],
	"cpAvg":58,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2644,
	"isProvisional":false
}, {
	"_id":"ODFhzeYU",
	"moveTimes":[40,30,60,10,80,15,80,50,100,200,60,40,30,20,15,200,400,200,20,30,10,40,200,15],
	"evals":[15,10,99,109,116,81,62,110,74,104,110,68,144,144,125,308,155,78,70,137,44,55,101,1000],
	"diffs":[33,6,1,9,77,49,11,40,0,0,45,0,11,24,0,183,75,0,18,100,12,13,87,0],
	"cpAvg":33,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2101,
	"isProvisional":true
}, {
	"_id":"8iteYKSb",
	"moveTimes":[150,80,60,100,400,100,30,80,150,150,200,150,15,200,15,30,50,20,100,40,80,100,30,15,20,20,30,20,30,15,50,15,5,15,20,10,20,5,10,10,1],
	"evals":[-8,-54,-58,-22,2,26,6,45,19,50,78,58,53,48,20,44,-22,0,60,12,0,71,77,20,-8,18,0,0,125,144,229,214,192,1000,1000,1000,1000,1000,1000,1000,1000],
	"diffs":[43,3,7,0,0,14,2,33,0,0,31,22,16,27,0,72,34,0,50,13,0,0,50,37,21,18,26,0,0,13,166,97,76,453,846,0,0,0,533,0,0],
	"cpAvg":65,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2121,
	"isProvisional":true
}, {
	"_id":"VJBN8tDX",
	"moveTimes":[60,40,100,80,150,10,30,30,40,150,300,40,200,150],
	"evals":[15,-26,-31,-2,13,-32,-37,-5,20,-64,641,1000,1000,1000],
	"diffs":[41,0,6,5,41,21,0,13,95,49,0,0,0,0],
	"cpAvg":19,
	"blurs":0,
	"holdAlert":false,
	"isWinner":true,
	"rating":2228,
	"isProvisional":true
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

output = {'decision': json.dumps(input_data), 'cheatPercent': 20}
print json.dumps(output)
