# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:59:09 2017

@author: Administrator
"""

import numpy as np 
from sklearn.datasets import load_digits 
from sklearn.metrics import confusion_matrix, classification_report 
from sklearn.preprocessing import LabelBinarizer 
from NeuralNetworkSaveWeigths import NeuralNetworkSaveWeigths
from sklearn.cross_validation import train_test_split


digits = load_digits()  
X = digits.data  
y = digits.target  
print(X)
X -= X.min() # normalize the values to bring them into the range 0-1  
print(X)
X /= X.max()
print(X)


nn = NeuralNetworkSaveWeigths([64,100,10],'HandwrittenDigitsReconnition_Weigths','logistic')  
X_train, X_test, y_train, y_test = train_test_split(X, y)  
labels_train = LabelBinarizer().fit_transform(y_train)  
labels_test = LabelBinarizer().fit_transform(y_test)
print("start fitting")
nn.fit(X_train,labels_train,epochs=3000)  
predictions = []  
for i in range(X_test.shape[0]):  
    o = nn.predict(X_test[i] )  
    predictions.append(np.argmax(o))  
print(confusion_matrix(y_test,predictions)  )
print(classification_report(y_test,predictions))
