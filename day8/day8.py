import os
import time
from math import lcm

def task1():
    with open('day8.txt', 'r') as file_in:
        network = {}
        currentLocation, idx, steps = 'AAA', 0, 0

        lines = file_in.readlines()
        instructions = lines[0].strip()

        for line in lines[2:]:
            src, dest = line.strip().split(' = ')[0], line.strip().split(' = ')[1].strip('()').split(', ')
            directions = {'L': dest[0], 'R': dest[1]}
            network[src] = directions

        while currentLocation != 'ZZZ':
            instruction = instructions[idx]
            currentLocation = network[currentLocation][instruction]
            idx = (idx+1)%len(instructions)
            steps += 1

        return steps
    
# Would take aproximately 345 hours to complete
def task2():
    with open('day8.txt', 'r') as file_in:
        network = {}
        paths, idx, steps = [], 0, 0

        lines = file_in.readlines()
        instructions = lines[0].strip()

        for line in lines[2:]:
            src, dest = line.strip().split(' = ')[0], line.strip().split(' = ')[1].strip('()').split(', ')
            directions = {'L': dest[0], 'R': dest[1]}
            network[src] = directions
            if src[-1] == 'A':
                paths.append(src)
        
        while any(path[-1] != 'Z' for path in paths):
            paths = [network[path][instructions[idx]] for path in paths]
            idx = (idx+1)%len(instructions)
            steps += 1

        return steps
    
def findCycle(source, instructions, network):
    currentLocation, steps, idx = source, 1, 0
    while True:
        instruction = instructions[idx]
        currentLocation = network[currentLocation][instruction]
        if currentLocation[-1] == 'Z':
            break
        idx = (idx+1)%len(instructions)
        steps += 1

    return steps



def task2LCM():
    with open('day8.txt', 'r') as file_in:
        network = {}
        sources, destinations, idx, steps = [], [], 0, 0
        cycleLengths = []

        lines = file_in.readlines()
        instructions = lines[0].strip()

        for line in lines[2:]:
            src, dest = line.strip().split(' = ')[0], line.strip().split(' = ')[1].strip('()').split(', ')
            directions = {'L': dest[0], 'R': dest[1]}
            network[src] = directions
            if src[-1] == 'A':
                sources.append(src)
            if src[-1] == 'Z':
                destinations.append(src)

        for source in sources:
            cycleLengths.append(findCycle(source, instructions, network))

        return lcm(*cycleLengths)
            



        

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f'Task 1: {solution1}')

    # start = time.time()
    # solution2 = task2()
    # end = time.time()
    # print(f'Task 2: {solution2}')
    # print(f'Time: {end-start}')

    solution2 = task2LCM()
    print(f'Task 2: {solution2}')