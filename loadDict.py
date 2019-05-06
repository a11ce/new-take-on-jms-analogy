def loadDict():
    fitDict = {}
    with open("data/csv/fitness.csv") as infile:
        for line in infile:
            splitLine = line.split(",")
            
            fitDict[splitLine[0]] = int(splitLine[-1])
            
    return fitDict

if __name__ == "__main__":
    print(loadDict())