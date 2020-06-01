#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

# Finding the range for features 1 and 2
min_feature_2 = sys.maxint
min_feature_1 = sys.maxint
max_feature_2 = 0
max_feature_1 = 0
for p in data_dict:
    itFeat1 = data_dict[p][feature_1] 
    itFeat2 = data_dict[p][feature_2] 
    if (itFeat1 != "NaN"):
        if (itFeat1 < min_feature_1):
            min_feature_1 = itFeat1
        elif (itFeat1 > max_feature_1):
            max_feature_1 = itFeat1
    if (itFeat2 != "NaN"):
        if (itFeat2 < min_feature_2):
            min_feature_2 = itFeat2
        elif (itFeat2 > max_feature_2):
            max_feature_2 = itFeat2
print("Range for {} : {} - {}".format(feature_1, min_feature_1, max_feature_1))
print("Range for {} : {} - {}".format(feature_2, min_feature_2, max_feature_2))

# Feature scaling
from sklearn.preprocessing import MinMaxScaler
import numpy
feature_array=numpy.array(finance_features)
scaler = MinMaxScaler()
rescaled_feat = scaler.fit_transform(finance_features)
#print("Rescaled features : {}".format(rescaled_feat))
print("Scaled values for {}", scaler.transform([200000.0,1000000.0]))


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(finance_features)
# print("Labels : ", kmeans.labels_)
# print("Centroids : ", kmeans.cluster_centers_)
pred = kmeans.predict(finance_features)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters_2.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"