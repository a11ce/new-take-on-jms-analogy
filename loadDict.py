import os

def loadDict():
    fitDict = {}
    location = os.path.dirname(os.path.realpath(__file__))
    with open(location + "/data/csv/3percent.csv") as infile:
        for line in infile:
            splitLine = line.strip().split(",")
            if splitLine[0] != '':
                fitDict[splitLine[0].lower()] = int(splitLine[-1])
            
    return fitDict

if __name__ == "__main__":
    print(loadDict())