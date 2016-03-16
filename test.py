from weka.core.converters import Loader
import weka.core.jvm as jvm
from weka.classifiers import Classifier

jvm.start()

#loader = Loader(classname="weka.core.converters.JSONLoader")
#data = loader.load_file("test.json")
loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file("games.arff")
data.class_is_last()

print(data)

cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C","0.3"])
cls.build_classifier(data)

for index, inst in enumerate(data):
	pred = cls.classify_instance(inst)
	dist = cls.distribution_for_instance(inst)
	print(str(index+1) + ": label index=" + str(pred) + ", class distribution=" + str(dist))

jvm.stop()
