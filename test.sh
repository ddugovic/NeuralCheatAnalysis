python convert.py > games.arff
python test.py
#python /usr/local/lib/python2.7/dist-packages/weka/classifiers.py -t ./game.arff -c last weka.classifiers.trees.J48 -C 0.3
#python /usr/local/lib/python2.7/dist-packages/weka/classifiers.py -t ./game.arff -c last weka.classifiers.functions.MultilayerPerceptron -L 0.1 -M 0.2 -N 5000 -V 0 -S 0 -E 20 -H 2 -R
#python /usr/local/lib/python2.7/dist-packages/weka/classifiers.py -t ./game.arff -c last weka.classifiers.functions.MultilayerPerceptron -S `date '+%s'`
