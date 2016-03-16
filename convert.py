import json
import random

# This file is used for converting JSON to ARFF until I can figure out how to make JSONLoader work.
# The final attribute "group" is the class (in training data)
M = 3
N = 50
header = """
@relation lichess.games

@attribute cpAvg numeric
@attribute blurs numeric
@attribute holdAlert {false,true}
@attribute isWinner {false,true}
@attribute rating numeric
@attribute isProvisional {false,true}
"""
for n in range(0,N):
	header += "@attribute mt%d numeric\n" % (n+1)
for n in range(0,N):
	header += "@attribute ev%d numeric\n" % (n+1)
for n in range(0,N):
	header += "@attribute df%d numeric\n" % (n+1)
header += """@attribute group {0,1}

@data
"""

print header
for filename in ["game1.json","game2.json","game3.json"]:
	with open(filename) as json_file:
		json_data = json.load(json_file)
		json_data["moveTimes"] += ['?'] * (N - len(json_data["moveTimes"]))
		json_data["evals"] += ['?'] * (N - len(json_data["evals"]))
		json_data["diffs"] += ['?'] * (N - len(json_data["diffs"]))
		output = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (json_data["cpAvg"], json_data["blurs"], str(json_data["holdAlert"]).lower(), str(json_data["isWinner"]).lower(), json_data["rating"], str(json_data["isProvisional"]).lower(), ','.join(map(str,json_data["moveTimes"][:N])), ','.join(map(str,json_data["evals"][:N])), ','.join(map(str,json_data["diffs"][:N])), random.randint(0,1))
		for i in range(0,M):
			print output
