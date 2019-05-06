import string

import loadDict

def main():
    fitDict = loadDict.loadDict()
    goodPos, badPos = possibleMutations(fitDict, "nest")
    print("best")
    print(goodPos)
    print(badPos)

def possibleMutations(fitDict, word):
    inFit = fitDict[word]
    goodPos ={}
    badPos  ={}
    
    for index in range(len(word)):
        for newChar in string.ascii_lowercase:
        
            newWord = word[:index] + newChar + word[index + 1:]
            if(newWord in fitDict):
                 
                if(fitDict[newWord] > inFit):
                    goodPos[newWord] = fitDict[newWord]
                else:
                
                    badPos[newWord] = fitDict[newWord]
    return goodPos, badPos
    
if __name__ == "__main__":
    main()