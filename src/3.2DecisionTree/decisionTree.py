# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:04:51 2017

@author: Administrator
"""

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
#from sklearn.externals.six import StringIO

def TestDecisionTree():    
    # Read in the csv file and put featres in a list of dict 
    allElectronicsData=open('E:/cs/Study/Python/MachineLearningBasics_MachineLaing/Datasets/allElectronics.csv','r')
    reader=csv.reader(allElectronicsData)
    headers = next(reader)
    
    print(headers)
   
    featureList=[]
    labelList=[]
    
    for row in reader:
        labelList.append(row[len(row)-1])
        rowDict={}
        for i in range(1,len(row)-1):
            rowDict[headers[i]]=row[i]
        featureList.append(rowDict)
        
    print(featureList)
    
    #Vetorize features 
    vec=DictVectorizer()
    dummyX =vec.fit_transform(featureList).toarray()
    
    print("dummyX:"+str(dummyX))
    print(vec.get_feature_names())
    
    #Vertorize class Labels
    lb=preprocessing.LabelBinarizer()
    dummyY=lb.fit_transform(labelList)
    print("dummyY:"+str(dummyY))
    
    #Using decision tree for classfication 
    clf=tree.DecisionTreeClassifier(criterion='entropy')
    clf=clf.fit(dummyX,dummyY)
    print("clf:"+str(clf))
    
    #Visulize model
    with open("allElectronicInformationGainOri.dot","w") as f:
        f=tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

   
    oneRowX=dummyX[0,:]
    print("oneRowX: "+str(oneRowX))
    
    newRowX=oneRowX
    newRowX[0]=1
    newRowX[2]=0
    print("newRowsX: "+str(newRowX))
    
    predictedY=clf.predict([newRowX])
    print("predictedY: "+str(predictedY))
    
if __name__=='__main__':
    TestDecisionTree()
    #print("ddd")




