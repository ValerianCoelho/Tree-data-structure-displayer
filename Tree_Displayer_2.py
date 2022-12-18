import math

def logOfPowerSeries(noOfTerms):
    return int(math.log(noOfTerms + 1, 2))

def sumOfPowerSeries(noOfTerms):
    return pow(2, noOfTerms) - 1

levelOrder = input().split(' ') # Taking input from the user in level order sequence
levelOrder = [levelOrder[sumOfPowerSeries(i):sumOfPowerSeries(i+1)] for i in range(logOfPowerSeries(len(levelOrder)))] # Splitting the List (levelOrder) into sub-list's, replicating Level order traversal structure

width = []

for i in range(len(levelOrder)-1, -1, -1):
    top = ''; center = ''; bottom = ''
    line = []

    for j in range(len(levelOrder[i])):
        # Top ----------------------------
        if i == 0: # Belongs to a root node
            top = top + '┌' + '─'*(len(levelOrder[i][j])+2) + '┐'
        else: # Belongs to a non-root node
            top = top + '┌' + f'{"┴":─^{len(levelOrder[i][j])+2}}' + '┐'

        # Center -------------------------
        center = center + '│ ' + levelOrder[i][j] + ' │'
            
        # Bottom -------------------------
        if i == len(levelOrder)-1: # Belongs to a leaf node
            bottom = bottom + '└' + '─'*(len(levelOrder[i][j])+2) + '┘'

            # Appending the width of every node, The width is calculated here because this 'if block' runs only once at the start of the for loop, and that is what we want
            width.append(len('│ ' + levelOrder[i][j] + ' │'))

        else: # Belongs to a non-leaf node
            bottom = bottom + '└' + f'{"┬":─^{len(levelOrder[i][j])+2}}' + '┘'

        # Adding the width between nodes, this is done only when the level in not a leaf level
        if i != len(levelOrder)-1:
            top = f'{top: ^{width[2*j]+width[2*j+1]+1}}'
            center = f'{center: ^{width[2*j]+width[2*j+1]+1}}'
            bottom = f'{bottom: ^{width[2*j]+width[2*j+1]+1}}'

        # Adding one whitespace padding between nodes
        if j != len(levelOrder[i])-1:
            top += ' '; center += ' '; bottom += ' '

    print(top)
    print(center)
    print(bottom)
    print(width)

# lines-> line-> (top, center, bottom)

# 1 2 3 4 5 6 7
# ['4', '5', '6', '7']
# ['2', '3']
# ['1']