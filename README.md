# NeuralCheatAnalysis

This script will take an unsorted list of game assessments (only some of the fields from a full GameAssessment are required) from a single player and will return whether the player should be reported, marked, or no-action.

The names of the fields are the same as what is stored in mongoDB on lila.

Input format (JSON):
```javascript
[
	{
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
		... // more game assessments
	}
]
```

This data is to be POSTed to the script with the field name 'input'.
All fields for each entry must be populated (no assuming default values).

This script will then output one of the following:
NO-ACTION
REPORT
MARK

ToDo: Build web interface. Most of the ground work for the interface is done, just set input_text to the JSON input