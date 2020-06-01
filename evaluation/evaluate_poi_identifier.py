#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys='../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)

### your code goes here 
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(features,labels,test_size=0.3, random_state=42)

from sklearn import tree
classifier = tree.DecisionTreeClassifier()
classifier.fit(x_train, y_train)
pred = classifier.predict(x_test)

print("Total number in test set : ", len(x_test))
print("Predictions equal to 1 : ", np.where(pred == 1.0)[0])
print("Samples equal to 1 in test set : ", np.where(np.array(y_test) == 1.0)[0])

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,pred)
print("Accuracy : ", accuracy)

from sklearn.metrics import precision_score
precision = precision_score(y_test,pred)
print("Precision : ", precision)

from sklearn.metrics import recall_score
recall = recall_score(y_test,pred)
print("Recall : ", recall)