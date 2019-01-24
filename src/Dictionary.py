'''
Created on Oct 6, 2015

This is a class to implement a dictionary with various utility functions

@author: Trant
'''
import os

class Dictionary:
    'A dictionary of words with utility functions'
    def __init__(self):
        self.words = []
        homedir = os.environ['HOMEPATH']
        dataFile = '..\\data\\smallDictionary.txt'
        dFile = open(dataFile, 'r')
        for line in dFile:
            line = line.strip() 
            self.words.append(line)
        return
    
    def listByLength(self, wordWidth):
        localList = []
        for word in self.words:
            if (len(word) == wordWidth):
                localList.append(word)
        return localList

