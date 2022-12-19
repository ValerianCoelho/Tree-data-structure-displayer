import math

# 2^0 + 2^1 + 2^3 = 1 + 2 + 4 = 7
# logOfPowerSeries(7) = 3 , where '3' is the number of terms added to get 7
# logOfPowerSeries() function is used to calculate the height of the binary tree, for no of inputs = 7, height = 3

def logOfPowerSeries(noOfTerms): 
    return int(math.log(noOfTerms + 1, 2))

# 2^0 + 2^1 = 1 + 2  = 3
# sumOfPowerSeries(2) = 3, where 3 is the summation of all the first 2 terms

def sumOfPowerSeries(noOfTerms):
    return pow(2, noOfTerms) - 1

# printLevel(level) prints an entire level of a strict binary tree
# a level is a list divided into 3 parts; top center and bottom
# ┌───┐ -> top
# │ 1 │ -> center
# └───┘ -> bottom

def printLevel(level):
    for l in level:
        print(l)

# Takes input from the user in level order sequence
levelOrder = input().split(' ') 

# Divides the input taken from the user into many sub-lists, representing the different levels of a strict binary tree
levelOrder = [levelOrder[sumOfPowerSeries(i):sumOfPowerSeries(i+1)] for i in range(logOfPowerSeries(len(levelOrder)))] 

# 'levels' is a list that will hold all the levels of the strict binary tree
#                                       ┌────────┐
#                                       │ levels │
#                                       └───┬────┘
#             ┌─────────────────────────────┼─────────────────────────────┐
#         ┌───┴───┐                     ┌───┴───┐                     ┌───┴───┐
#         │ level │                     │ level │                     │ level │
#         └───┬───┘                     └───┬───┘                     └───┬───┘
#     ┌───────┼──────────┐          ┌───────┼──────────┐          ┌───────┼──────────┐
# ┌───┴─┐ ┌───┴────┐ ┌───┴────┐ ┌───┴─┐ ┌───┴────┐ ┌───┴────┐ ┌───┴─┐ ┌───┴────┐ ┌───┴────┐
# │ top │ │ center │ │ bottom │ │ top │ │ center │ │ bottom │ │ top │ │ center │ │ bottom │
# └─────┘ └────────┘ └────────┘ └─────┘ └────────┘ └────────┘ └─────┘ └────────┘ └────────┘

levels = []

# 'edges' is a list that will hold all the edge links of the strict binary tree
# eg : '┌────┴─────┐'
edges = []

# 'width' is a list that will hold the width's of all the nodes of a strict binary tree
width = []

# Iterating through every level of the strict binary tree
for i in range(len(levelOrder)-1, -1, -1):

    top = ''; center = ''; bottom = ''; edge = ''
    level = []

    # Iterating through every node of a level
    for j in range(len(levelOrder[i])):

        # These are going to hold the string values of every individual node
        subTop = ''; subCenter = ''; subBottom = ''

        # Top ----------------------------
        if i == 0: # Belongs to a root node
            subTop = '┌' + '─'*(len(levelOrder[i][j])+2) + '┐'
        else: # Belongs to a non-root node
            subTop = '┌' + f'{"┴":─^{len(levelOrder[i][j])+2}}' + '┐'

        # Center -------------------------
        subCenter = '│ ' + levelOrder[i][j] + ' │'
            
        # Bottom -------------------------
        if i == len(levelOrder)-1: # Belongs to a leaf node
            subBottom = '└' + '─'*(len(levelOrder[i][j])+2) + '┘'

            # Appending the width of every node, The width is calculated here because this 'if block' runs only once at the start of the for loop, and that is what we want
            width.append(len('│ ' + levelOrder[i][j] + ' │'))

        else: # Belongs to a non-leaf node
            subBottom = '└' + f'{"┬":─^{len(levelOrder[i][j])+2}}' + '┘'

        # Adding the padding for non-leaf nodes -------------------------
        if i != len(levelOrder)-1:
            subTop = f'{subTop: ^{width[j]}}'
            subCenter = f'{subCenter: ^{width[j]}}'
            subBottom = f'{subBottom: ^{width[j]}}'

        # Adding the sub-(top, center and bottom) to (top, center, bottom)
        top += subTop; center += subCenter; bottom += subBottom

        # Adding one whitespace padding between nodes
        if j != len(levelOrder[i])-1:
            top += ' '; center += ' '; bottom += ' '

    # Appending the top, center and bottom to 'level' 
    level.append(top)
    level.append(center)
    level.append(bottom)

    # Inserting a new 'level' at the start of the list levels, since we are iterating from n-1 to 0
    levels.insert(0, level)

    # Edges -------------------------

    # The edges won't be added for the leaf nodes
    if i != len(levelOrder)-1:

        for k in range(len(width)):
            
            margin = sum(width[0:k])+k

            # charType = 1  => ' '
            # charType = -1 => '─'

            charType = -1

            # Iterating through the width of the nodes below the current edge
            for t in range(width[k]):

                # Checks if a node below the edge has a '┴' socket
                if levels[1][0][t+margin] == '┴':
                    if charType == -1:
                        edge += '┌'
                    else:
                        edge += '┐'
                    charType *= -1

                elif levels[0][2][t+margin] == '┬':
                    edge += '┴'
                
                elif charType == 1:
                    edge += '─'
                elif charType == -1:
                    edge += ' '
            edge += ' '
    edges.insert(0, edge)
    
    # Merging the width of two lower nodes into one 
    # eg: before :  width = [5, 5, 5, 5]

    width = [width[2*x]+width[2*x+1]+1 for x in range(int(len(width)/2))]

    # after : width = [10, 10]


for i in range(len(levels)):
    printLevel(levels[i])
    if i != len(levels)-1:
        print(edges[i])