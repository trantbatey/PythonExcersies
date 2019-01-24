'''
Created on Oct 6, 2015

This is a Graph Node class. It is intended
to be used to do word ladder searches in a dictionary.

@author: Trant
'''
import Dictionary

class Node:
    'A tree graph implementation of words searches'
    dictionary = []
    masterList = []
    listOfLists = []
    currentList = []
    queue = []
    numLadders = 0
    numFound = 0
    
    @classmethod
    def initNodeClass(self, lastWord, numLadders):
        Node.dictionary = Dictionary.Dictionary()
        Node.wordList = Node.dictionary.listByLength(len(lastWord))
        Node.numLadders = numLadders
        for word in Node.wordList:
            node = Node()
            node.word = word
            Node.masterList.append(node)

    def __init__(self):
        self.word = ""
        self.oneOff = []
        self.used = 0
        self.dead = 0
        self.previousNode = 0
        
    @classmethod
    def getNodeByWord(self, word):
        for node in Node.masterList:
            if node.word == word: return node

    def findLaddersByDepth(self, firstWord, lastWord):
        if Node.numFound == Node.numLadders: return
        node = self.getNodeByWord(firstWord)
        if node.dead: return
        Node.currentList.append(node)
        node.used = 1
        if (node.word == lastWord):
            Node.numFound += 1
            newList = Node.currentList[:]
            Node.listOfLists.append(newList)
            Node.printWordLadder(newList)
        else:
            try:
                node.oneOff = node.getOneLetterOff()
                numFoundByNode = Node.numFound
                for newNode in node.oneOff:
                    newNode.findLaddersByDepth(newNode.word, lastWord)
                if numFoundByNode == Node.numFound: self.dead = 1
            except GraphClassInitError, arg:
                print arg
        Node.currentList.pop()
        node.used = 0
        return
    
    def findLaddersByBredth(self, firstWord, lastWord):
        Node.queue.insert(0,self.getNodeByWord(firstWord)) # enqueue first node
        while (Node.queue):
            node = Node.queue.pop()
            if node.used: continue
            node.used = 1
            #print("word: %s " % (node.word))
            if (node.word == lastWord):
                Node.numFound += 1
                Node.printLinkedLadder(node)
                if Node.numFound == Node.numLadders: return
            else:
                try:
                    node.oneOff = node.getOneLetterOff()
                    for newNode in node.oneOff:
                        newNode.previousNode = node
                        Node.queue.insert(0,newNode)
                except GraphClassInitError, arg:
                    print arg
        return
    
    def getOneLetterOff(self):
        oneOffList = []
        if len(Node.masterList) == 0: 
            raise GraphClassInitError("Tree Class Not Initialized")
        for thisNode in Node.masterList:
            if not thisNode.used:
                i = 0 
                notMatched = 0
                while i < len(thisNode.word):
                    if thisNode.word[i] != self.word[i]: 
                        notMatched += 1
                    if notMatched == 2: break
                    i += 1
                if notMatched == 1:
                    oneOffList.append(thisNode)
        return oneOffList
    
    @classmethod
    def printWordLadder(self, nodeList):
        print "Ladders #", Node.numFound
        i = 1
        end = len(nodeList)
        for node in nodeList:
            if i != end: print node.word + " -> ",
            else: print node.word + "\n"
            if i%5 == 0:
                print ""
            i += 1
        print ""
        return
    
    @classmethod
    def printLinkedLadder(self, nodeIn):
        print "Ladders #", Node.numFound
        
        node = nodeIn
        printList = []
        printList.insert(0,node.word)
        while (node.previousNode):
            node = node.previousNode
            printList.insert(0,node.word)
        
        i = 1
        end = len(printList)
        for word in printList:
            if i != end: print word + " -> ",
            else: print word + "\n"
            if i%5 == 0:
                print ""
            i += 1
        print ""
        return
 
class GraphClassInitError(RuntimeError):
    
    def __init__(self, arg):
        self.args = arg
        
        