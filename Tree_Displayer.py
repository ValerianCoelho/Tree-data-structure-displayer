import math

def logOfPowerSeries(noOfTerms):
    return int(math.log(noOfTerms + 1, 2))

def sumOfPowerSeries(noOfTerms):
    return pow(2, noOfTerms) - 1

levelOrder = input().split(' ') # Taking input from the user in level order sequence
levelOrder = [int(node) for node in levelOrder] # Typecasting all the input to int
levelOrder = [levelOrder[sumOfPowerSeries(i):sumOfPowerSeries(i+1)] for i in range(logOfPowerSeries(len(levelOrder)))] # Splitting the List (levelOrder) into sub-list's, replicating Level order traversal structure

lines = []
width = []

for i in range(len(levelOrder)-1, -1, -1):
    line = []
    top = ''
    center = ''
    bottom = ''
    line = []
    if i == len(levelOrder)-1: # This is a leaf node

        for j in range(len(levelOrder[i])): # Creating the top and bottom portion of the box

            top += '┌' + f'{"┴":─^{len(str(levelOrder[i][j]))+2}}' + '┐'
            center += '│ ' + str(levelOrder[i][j]) + ' │'
            bottom += '└' + '─'*(len(str(levelOrder[i][j]))+2) + '┘'

            if j!=len(levelOrder[i])-1:
                bottom += ' '
                top += ' '
                center += ' '
    if i == 0: # This is a root node
        print('Hello')
    else: # This is for non-(root, leaf) nodes
        print('Hello')


    line.append(top)
    line.append(center)
    line.append(bottom)
    lines.append(line)

print(lines)

# print(levelOrder)
# print(nodeLinesSum)


# lines-> line-> (top, center, bottom)