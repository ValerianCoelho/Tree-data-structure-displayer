import math

def logOfPowerSeries(noOfTerms):
    return int(math.log(noOfTerms + 1, 2))

def sumOfPowerSeries(noOfTerms):
    return pow(2, noOfTerms) - 1

levelOrder = input().split(' ') # Taking input from the user in level order sequence
levelOrder = [levelOrder[sumOfPowerSeries(i):sumOfPowerSeries(i+1)] for i in range(logOfPowerSeries(len(levelOrder)))] # Splitting the List (levelOrder) into sub-list's, replicating Level order traversal structure

lines = []
width = []
edges = []

for i in range(len(levelOrder)-1, -1, -1):
    top = ''; center = ''; bottom = ''
    line = []
    edge = ''

    for j in range(len(levelOrder[i])):
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

        # Adding the width between nodes, this is done only when the level in not a leaf level
        if i != len(levelOrder)-1:
            # Bug encountered here, here j = 1, so width[2*j+1] will be out of range
            subTop = f'{subTop: ^{width[j]}}'
            subCenter = f'{subCenter: ^{width[j]}}'
            subBottom = f'{subBottom: ^{width[j]}}'

            

        # Adding the sub-(top, center and bottom) to (top, center, bottom)
        top += subTop; center += subCenter; bottom += subBottom

        # Adding one whitespace padding between nodes
        if j != len(levelOrder[i])-1:
            top += ' '; center += ' '; bottom += ' '
    if i != 0:
        edgeWidth = [sum(width[0:k]) + k + int(width[k]/2) for k in range(len(width))]
        for k in range(int(len(levelOrder[i])/2)):
            subEdge = ' '*int((width[2*k])/2) + '┌' + f'{"┴":─^{edgeWidth[2*k+1]-edgeWidth[2*k]-1}}' + '┐' + ' '*(int(width[2*k+1]/2)) + ' '
            edge += subEdge
        edges.append(edge)
        

    width = [width[2*x]+width[2*x+1]+1 for x in range(int(len(width)/2))]

    line.append(top)
    line.append(center)
    line.append(bottom)

    lines.append(line)

lines.reverse()
edges.reverse()



for i in range(len(lines)):
    if i != 0:
        print(edges[i-1])
    for j in range(len(lines[i])):
        print(lines[i][j])
    
# lines-> line-> (top, center, bottom)

# print(edges)
# print(lines)

# 1 2 3 4 5 6 7
# ['4', '5', '6', '7']
# ['2', '3']
# ['1']