import os

def loadDict():
    fitDict = {}
    location = os.path.dirname(os.path.realpath(__file__))
    with open(location + "/data/csv/filtered-2000.csv") as infile:
        for line in infile:
            splitLine = line.split(",")
            
            fitDict[splitLine[0]] = int(splitLine[-1])
            
    return fitDict

if __name__ == "__main__":
    print(loadDict())