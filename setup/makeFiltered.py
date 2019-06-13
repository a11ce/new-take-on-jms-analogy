import numpy as np
import matplotlib.pyplot as plt
import sys

cutoff = 800
whichCsv = sys.argv[1]

nums = []
lines = []

with open("../data/csv/" + whichCsv, 'r') as csv:
    for line in csv:
        num = int(line.rstrip().split(",")[1])
        if(num > cutoff):
            lines.append(line)
            nums.append(num)
            print(line)

with open("../data/csv/filtered-" + whichCsv, 'w') as outCsv:
    for line in lines:
        outCsv.write(line)

print(len(nums))
#plt.show(plt.hist(nums, bins = "auto"))
