'''
Created on Oct 6, 2015

This is a WordTree class that includes the Leaf sub-class. It is intended
to be used to do word searches in a dictionary.

@author: Trant
'''
import Dictionary

class WordTree:
    'A tree structure of words with any number of branches'
    dictionary = []
    masterList = []
    listOfLists = []
    currentList = []
    lastWord = ""
    numLadders = 0
    numFound = 0
    
    @classmethod
    def initWordTreeClass(self, theLastWord, numLadders):
        WordTree.lastWord = theLastWord
        WordTree.dictionary = Dictionary.Dictionary()
        WordTree.masterList = WordTree.dictionary.listByLength(len(theLastWord))
        WordTree.numLadders = numLadders
        
    def __init__(self, word, level):
        self.word = word
        self.level = level
        self.nextLevel = []

    def findLaddersByLevel(self, currentLevel):
        if WordTree.numFound == WordTree.numLadders: return
        if self.level != currentLevel:
            for tree in self.nextLevel:
                WordTree.currentList.append(self.word)
                tree.findLaddersByLevel(currentLevel)
                WordTree.currentList.pop()
            return
        WordTree.currentList.append(self.word)
        if (self.word == WordTree.lastWord):
            WordTree.numFound += 1
            newList = WordTree.currentList[:]
            WordTree.listOfLists.append(newList)
        else:
            oneOff = []
            try:
                oneOff = self.getOneLetterOff()
                for newWord in oneOff:
                    self.nextLevel.append(WordTree(newWord, self.level+1))
            except TreeClassInitError, arg:
                print arg
        WordTree.currentList.pop()
        return
            
    
    def findWordLadders(self):
        currentLevel = 1
        while WordTree.numFound != WordTree.numLadders:
            self.findLaddersByLevel(currentLevel)
            currentLevel += 1
        return
            
    def getOneLetterOff(self):
        oneOffList = []
        if len(WordTree.masterList) == 0: 
            raise TreeClassInitError("Tree Class Not Initialized")
        for thisWord in WordTree.masterList:
            if WordTree.currentList:
                if thisWord not in WordTree.currentList:
                    i = 0 
                    notMatched = 0
                    while i < len(thisWord):
                        if thisWord[i] != self.word[i]: 
                            notMatched += 1
                        if notMatched == 2: break
                        i += 1
                    if notMatched == 1:
                        oneOffList.append(thisWord)
        return oneOffList
    
    @classmethod
    def printWordLadders(self):
        for wordList in WordTree.listOfLists:
            i = 1
            for word in wordList:
                if word != WordTree.lastWord: print word + " -> ",
                else: print word + "\n"
                if i%5 == 0:
                    print ""
                i += 1
        print ""
        return
    
class TreeClassInitError(RuntimeError):
   def __init__(self, arg):
      self.args = arg
        
        