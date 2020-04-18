#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
# To speed up training, sometimes we use a subset of all training examples. 
# Of course this impacts accuracy
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

# Training
train_starting_time = time()
from sklearn import svm

# Parameters
# classifier = svm.SVC(kernel='linear')
classifier = svm.SVC(kernel='rbf', C=10000.0)

classifier.fit(features_train, labels_train)
print("Training time: ", round(time() - train_starting_time, 3), "s")

# Prediction
prediction_starting_time = time()
predictions = classifier.predict(features_test)
print("Prediction time: ", round(time() - prediction_starting_time, 3), "s")

# Accuracy calculation
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,predictions)
print("Accuracy for algorithm : ", accuracy)

# Print specific predictions
print("Prediction for element 10: ", predictions[10])
print("Prediction for element 26: ", predictions[26])
print("Prediction for element 50: ", predictions[50])

# Summary of predictions
import numpy as np
print("Total number of predictions for class 0 : ", np.sum(predictions==0))
print("Total number of predictions for class 1 : ", np.sum(predictions==1))
#########################################################