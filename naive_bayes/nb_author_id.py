#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
# Training classifier
train_starting_time = time()
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train,labels_train)
print("Training time: ", round(time() - train_starting_time, 3), "s")

# Prediction
prediction_starting_time = time()
predictions = classifier.predict(features_test)
print("Prediction time: ", round(time() - prediction_starting_time, 3), "s")

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,predictions)
print("Accuracy is ", accuracy)
#########################################################


