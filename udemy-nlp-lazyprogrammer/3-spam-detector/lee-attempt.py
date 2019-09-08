# -*- coding: utf-8 -*-
from __future__ import print_function, division
from builtins import range
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier

from sklearn.feature_extraction.text import TfidfVectorizer

# Get raw data. Sentences is a 1D array of the 2nd column of all data
data = pd.read_csv('spam.csv', encoding = "ISO-8859-1").values
np.random.shuffle(data)
sentences = data[:,1]

# Fit and transform from sentences (input, i.e. X) to vocab array.
obj = TfidfVectorizer()
X = obj.fit_transform(sentences)

# Convert 1st column into an array where 'spam' = 1, of 'ham' = 0. Probably a more elegant way to do this!
rawColumn = data[:,0]
Y = []
for rawOrigin in rawColumn:
    if rawOrigin == 'spam' :
        Y.append(1)
    else:
        Y.append(0)

testNumber = 2000
Xtrain = X[:-testNumber,]
Ytrain = np.array(Y)[:-testNumber,]
Xtest = X[-testNumber:,]
Ytest = np.array(Y)[-testNumber:,]    

# Method 1
model = MultinomialNB()
model.fit(Xtrain, Ytrain)
print("Classification rate for NB:", model.score(Xtest, Ytest))

# Method 2
model = AdaBoostClassifier()
model.fit(Xtrain, Ytrain)
print("Classification rate for AdaBoost:", model.score(Xtest, Ytest))