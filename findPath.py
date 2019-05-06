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
    recursiveTreeSearch(startWord, endWord, fitDict,path )
    print(path)
def recursiveTreeSearch(root, target, fitDict, pathArr):
    pathArr.append(root)
    if(root == target):
        return True

    children, _ = findMutations.possibleMutations(fitDict, root)
    for child in children:
        
        if recursiveTreeSearch(child, target, fitDict, pathArr):
            return True
            
    pathArr.pop(-1)
    return False
    
if __name__ == "__main__":
    main()