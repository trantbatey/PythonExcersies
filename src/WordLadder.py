'''
Created on Oct 6, 2015

@author: Trant
'''
import time, calendar, WordTree, WordGraph, sys

# create a function to test file read and write
def fileIOTest () :
    text = raw_input("Enter a test string: ")
    fOut = open("testData.dat", "w")
    fOut.write(text)
    fOut.close()
    fIn = open("testData.dat", "r")
    text = fIn.read()
    print(text)
    fIn.close()
    return

def treeWordLadder (fisrtWord, lastWord):
    tree = WordTree.WordTree(fisrtWord, 1)
    tree.initWordTreeClass(fisrtWord,5)
    tree.findWordLadders()
    tree.printWordLadders()

def graphWordLadder (fisrtWord, lastWord):
    sys.setrecursionlimit(10000) 
    graph = WordGraph.Node()
    graph.initNodeClass(lastWord,10)
    graph.findLaddersByBredth(fisrtWord, lastWord)

def main():
    print
    print ("Hello from script.")
    
    print
    var1 = 'Hello World!'
    var2 = "Python Programming"
    print "var1[0]: ", var1[0]
    print "var2[1:5]: ", var2[1:5]
    
    print
    L = ['spam', 'Spam', 'SPAM!']
    print L[-2]
    
    print
    ticks = time.time()
    print "Number of ticks since 12:00am, January 1, 1970:", ticks
    
    print
    localtime = time.localtime(time.time())
    print "Local current time :", localtime
    
    print
    cal = calendar.month(2008, 1)
    print "Here is the calendar:"
    print cal
    
    #print
    #fileIOTest()

    #print
    #print "Tree Solution"
    #treeWordLadder("pit", "fin")

    print
    print "Graph Solution"
    graphWordLadder("mean", "sent")
    
if __name__ == '__main__':
    main()