#!/usr/bin/env python
# coding: utf-8

# In[11]:

# load dataset  module
# This modules loads the dataset from the given file and returns it as a nested dictionary.

def loadDataset():
    #open and read the file here
    try:
        textFile = open('transaction.txt', 'r')
    #make an empty dictionary
        myDict = {}
    #loop through the file and load the dataset into the empty dictionary
    
        for line in textFile:
            [userId, TransId, Description, Amt, xCoord, yCoord, fraud] = line.split(':')
            myDict.setdefault(userId, {})
            myDict[userId][TransId] = Description, float(Amt), float(xCoord), float(yCoord), fraud.strip("\n")
       
    #return the dictionary containing theh new data
        return myDict
    except:
        print('File error: ' + str(ioerr))  
        
     #Close the file
    textFile.close()
            
 # In[ ]:


