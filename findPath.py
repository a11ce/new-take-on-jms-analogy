import loadDict
import findMutations
import sys



def main():
    startWord = sys.argv[1]
    endWord   = sys.argv[2]
    
    fitDict = loadDict.loadDict()

    if(fitDict[startWord] > fitDict[endWord]):
        print("No path possible, startWord fitness is higher than endWord fitness")
        return
    path = []
    badArr = []
    recursiveTreeSearch(startWord, endWord, fitDict,path,badArr )
    print(path)
    
def recursiveTreeSearch(root, target, fitDict, pathArr, badArr):
    pathArr.append(root)
    if(root == target):
        return True

    children, _ = findMutations.possibleMutations(fitDict, root)
    for child in children:
        if child not in badArr:
            if recursiveTreeSearch(child, target, fitDict, pathArr, badArr):
                return True

            
    badArr.append(pathArr.pop(-1))
    return False
    
if __name__ == "__main__":
    main()