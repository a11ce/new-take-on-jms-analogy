import loadDict
import findMutations
import random
import sys

fitDict = loadDict.loadDict()

def main():

    startWord = sys.argv[1]
    print(randomPath(startWord))   

def randomPath(startWord):
    curWord = startWord
    path = []
    while True:
        goodPos, badPos = findMutations.possibleMutations(fitDict, curWord)
        path.append(curWord)
        if (len(goodPos) == 0):
            return path
        curWord = random.choice(list(goodPos.keys()))

def randomPathWithLength(startWord, length):
    while True:
        path = randomPath(startWord)
        if (len(path) > length):
            return path

def randomWord():
    return random.choice(list(fitDict.keys()))

def validatePath(path):
    for pairInd in range(len(path)-1):
        w1 = path[pairInd]
        w2 = path[pairInd+1]
        
        if not w1 in fitDict:
            print(w1 + " not in dict")
            return False
            
        if sum( w1[i] != w2[i] for i in range(len(w1)) ) != 1:
            print(str(w1) + " and " + str(w2) +" bad pair")
            return False

    return True
    
def sortList(arr):

    tempDict = {}
    for word in arr:
        tempDict[word] = fitDict[word]

    return sorted(tempDict, key=tempDict.get)
    
    
if __name__ == "__main__":
    main()