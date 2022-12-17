import math

def logOfPowerSeries(noOfTerms):
    return int(math.log(noOfTerms + 1, 2))

def sumOfPowerSeries(noOfTerms):
    return pow(2, noOfTerms) - 1

levelOrder = input().split(' ') # Taking input from the user in level order sequence
levelOrder = [int(node) for node in levelOrder] # Typecasting all the input to int
levelOrder = [levelOrder[sumOfPowerSeries(i):sumOfPowerSeries(i+1)] for i in range(logOfPowerSeries(len(levelOrder)))] # Splitting the List (levelOrder) into sub-list's, replicating Level order traversal structure

nodeLinesSum = []

for i in range(len(levelOrder)-1, -1, -1): # creating the body of all the numbers 
    nodeLineSum = ''
    for j in range(len(levelOrder[i])):
        nodeLineSum += '│ ' + str(levelOrder[i][j]) + ' │'
    nodeLinesSum.append(nodeLineSum)

print(levelOrder)
print(nodeLinesSum)