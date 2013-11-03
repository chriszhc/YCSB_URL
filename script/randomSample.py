import sys
usage = "randomSample.py <source file> <target number>"

print usage
fileName = sys.argv[1]
targetNumber = int (sys.argv[2])

f = open(fileName, 'r')
lines = f.readlines()
sourceNumber = len(lines)
print "%d / %d" % (targetNumber, sourceNumber)
prob = 1.0 * targetNumber / sourceNumber

import random

outputCount = 0;
for line in lines:
    dice = random.random();
    # print dice
    if (dice < prob) :
        #choose this line
        print line[:-1]
	outputCount += 1
    if (outputCount == targetNumber) :
        break





