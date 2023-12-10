import os
from copy import deepcopy

def getNeighbours(pipeMap, node):
    if pipeMap[node[0]][node[1]] == "F":
        return [(node[0], node[1]+1), (node[0] + 1, node[1])]
    elif pipeMap[node[0]][node[1]] == "L":
        return [(node[0], node[1]+1), (node[0] - 1, node[1])]
    elif pipeMap[node[0]][node[1]] == "J":
        return [(node[0], node[1]-1), (node[0] - 1, node[1])]
    elif pipeMap[node[0]][node[1]] == "7":
        return [(node[0], node[1]-1), (node[0] + 1, node[1])]
    elif pipeMap[node[0]][node[1]] == "|":
        return [(node[0] + 1, node[1]), (node[0] - 1, node[1])]
    elif pipeMap[node[0]][node[1]] == "-":
        return [(node[0], node[1]+1), (node[0], node[1]-1)]

def dfs(func, pipeMap, q=[], steps = 0, visited=set()):
    while q:
        node = q.pop(0)
        if node not in visited:
            visited.add(node)
            steps += 1
            for neighbour in func(pipeMap, node):
                q.append(neighbour)
    return steps, visited
    
def replaceS(pipeMap, node):
    entries = []
    vonNeumannNeighbour = {"right" : (0, 1), "left" : (0, -1), "down" : (1, 0), "up" : (-1, 0)}
    possiblePipes = {"right": ["7", "J", "-"], "left": ["L", "F", "-"], "down": ["L", "J", "|"], "up": ["F", "7", "|"]}
    for direction, coords in vonNeumannNeighbour.items():
        pipe = pipeMap[node[0] + coords[0]][node[1] + coords[1]]
        if pipe in possiblePipes[direction]:
            entries.append(direction)

    if entries[0] == "right":
        temp = set(possiblePipes["left"])
    else:
        temp = set(possiblePipes["right"])

    if entries[1] == "down":
        temp = temp.intersection(set(possiblePipes["up"]))
    else:
        temp = temp.intersection(set(possiblePipes["down"]))

    pipeMap[node[0]] = pipeMap[node[0]].replace("S", temp.pop())
    return pipeMap

def dilateMap(pipeMap, loop):
    vonNeumannNeighbour = {"right" : (0, 1), "left" : (0, -1), "down" : (1, 0), "up" : (-1, 0)}
    possiblePipes = {"right": ["7", "J", "-"], "left": ["L", "F", "-"], "down": ["L", "J", "|"], "up": ["F", "7", "|"]}
    possibleCandidates = set()
    rows, cols = len(pipeMap), len(pipeMap[0])

    dilated_array = [['.' for _ in range(cols * 2 + 1)] for _ in range(rows * 2 + 1)]

    for i in range(rows):
        for j in range(cols):
            pipe = "O" if (i, j) in loop else pipeMap[i][j]
            dilated_array[(i * 2)+1][(j * 2)+1] = pipe
            if pipe == "O":
                for dir, neighbour in vonNeumannNeighbour.items():
                    if 0 <= i + neighbour[0] < rows and 0 <= j + neighbour[1] < cols:
                        nextPipe = pipeMap[i + neighbour[0]][j + neighbour[1]]
                        if nextPipe in possiblePipes[dir] and ((i + neighbour[0], j + neighbour[1]) in loop):
                            dilated_array[(i * 2)+1 + neighbour[0]][(j * 2)+1 + neighbour[1]] = 'X'
            elif dilated_array[(i * 2)+1][(j * 2)+1] not in ["X", "O"]:
                dilated_array[(i * 2)+1][(j * 2)+1] = "C"
                possibleCandidates.add(((i * 2)+1, (j * 2)+1))
            
    return dilated_array, possibleCandidates

def detectOuterRegion(dilatedMap):
    vonNeumannNeighbour = {"right" : (0, 1), "left" : (0, -1), "down" : (1, 0), "up" : (-1, 0)}
    def regionFinder(dilatedMap, q, visited=set()):
        while q:
            node = q.pop(0)
            if node not in visited:
                visited.add(node)
                for neighbour in vonNeumannNeighbour.values():
                    neighbourCords = (node[0] + neighbour[0], node[1] + neighbour[1])
                    if 0 <= neighbourCords[0] < len(dilatedMap) and 0 <= neighbourCords[1] < len(dilatedMap[0]):
                        if dilatedMap[neighbourCords[0]][neighbourCords[1]] not in ["X", "O"]:
                            q.append(neighbourCords)
                            dilatedMap[neighbourCords[0]][neighbourCords[1]] = "#"
        with open('outerRegion.txt', 'w') as file_out:
            for row in dilatedMap:
                file_out.write(''.join(row) + '\n')
        return visited

    outsideNode = (0, 0)
    outsideRegion = regionFinder(dilatedMap, [outsideNode])
    return outsideRegion
    
def task1():
    with open('day10.txt', 'r') as file_in:
        pipeMap = file_in.readlines()
        for idx, line in enumerate(pipeMap):
            if "S" in line:
                start = (idx, line.find("S"))
        
        replaceS(pipeMap, start)
        result, _ = dfs(getNeighbours, pipeMap, [start])
        return (result + 1)//2
    
def task2():
    with open('day10.txt', 'r') as file_in:
        result2 = 0
        pipeMap = file_in.read().splitlines()
        for idx, line in enumerate(pipeMap):
            if "S" in line:
                start = (idx, line.find("S"))
        
        replaceS(pipeMap, start)
        _, loop = dfs(getNeighbours, pipeMap, [start])
        dilatedMap, candidates = dilateMap(pipeMap, loop)
        outerRegion = detectOuterRegion(dilatedMap)

        for candidate in candidates:
            if candidate not in outerRegion:
                result2 += 1
            else:
                dilatedMap[candidate[0]][candidate[1]] = " "

        with open('dilatedMap.txt', 'w') as file_out:
            for row in dilatedMap:
                file_out.write(''.join(row) + '\n')

        return result2
                


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f'Task 1: {solution1}')
    solution2 = task2()
    print(f'Task 2: {solution2}')