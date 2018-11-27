# -*- coding: utf-8 -*-

#Base modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Feature Extraction
from sklearn.preprocessing import LabelBinarizer

import sklearn.metrics as mlm

#just for testing/learning
from sklearn.neighbors import KNeighborsClassifier


from gensim.sklearn_api import LdaTransformer

import sys

workingdirectory = "C:\\Users\\Jeff Jarrard\\Documents\\GitHub\\NWU-Pacific\\NWU-Pacific" #Windows format
cfpbpath = "D:\\Data\\CFPB\\Consumer_Complaints.csv"
datapath = "D:\\Data\\NWU-Pacific\\"
ldaconfigfile = "C:\\Users\\Jeff Jarrard\\Documents\\GitHub\\NWU-Pacific\\NWU-Pacific\\processing\\configurations\\lda.json"
 #'/Users/juanhernandez/Development/NWU-Pacific/NWU-Pacific/processing/configurations/lda.json'
topicshdf = "D:\\Data\\NWU-Pacific\\topics.hdf"
#'/Users/juanhernandez/Development/NWU-Pacific/NWU-Pacific/' #Mac format
#print(sys.path) if you need to check to make sure all dependencies are loaded.
sys.path.insert(0,workingdirectory)

df_orig = pd.read_csv(cfpbpath)
df_topics = pd.read_hdf(topicshdf)
df_vectors = pd.read_hdf()

















#Example code from sklearn text

X_train = np.array([ [158, 64], [170, 86], [183, 84], [191, 80], [155, 49], [163, 59], [180, 67], [158, 54], [170, 67] ])
y_train = ['male', 'male', 'male', 'male', 'female', 'female', 'female',  'female', 'female']

plt.figure() 
plt.title('Human Heights and Weights by Sex') 
plt.xlabel('Height in cm') 
plt.ylabel('Weight in kg')
for i, x in enumerate(X_train): 
    # Use 'x' markers for instances that are male and diamond markers for instances that are female 
    plt.scatter(x[0], x[1], c='k', marker='x' if y_train[i] == 'male' else 'D') 
plt.grid(True) 
plt.show()

#Binarize the labels

lb=LabelBinarizer() 
y_train_binarized = lb.fit_transform(y_train)
y_train_binarized

K = 3

clf = KNeighborsClassifier(n_neighbors=K)
clf.fit(X_train, y_train_binarized.reshape(-1))


#Evaluate the model
#Accuracy - Precision - Recall

X_test = np.array([ [168, 65], [180, 96], [160, 52], [169, 67]]) 
y_test = ['male', 'male', 'female', 'female'] 
y_test_binarized = lb.transform(y_test)

predictions_binarized = clf.predict(X_test)
print('Test Labels: %s' % lb.inverse_transform(y_test_binarized))
print('Predicted Labels: %s' % lb.inverse_transform(predictions_binarized))


#Get the accuracy, precision, recall
print('Accuracy: %s' % mlm.accuracy_score(y_test_binarized,predictions_binarized))
print('Precision: %s' % mlm.precision_score(y_test_binarized,predictions_binarized))
print('Recall: %s' % mlm.recall_score(y_test_binarized,predictions_binarized))
print('F1 Score: %s' % mlm.f1_score(y_test_binarized,predictions_binarized))


from processing import semantic_models, tokenize

df = pd.read_csv(cfpbpath)
































