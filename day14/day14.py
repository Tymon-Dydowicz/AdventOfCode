from functools import reduce
import os
from re import finditer, sub

def tiltPlate(plate, direction):
    if direction in ['north', 'south']:
        plate = [''.join(line) for line in zip(*plate)]
    
    if direction in ['south', 'east']:
        plate = [line[::-1] for line in plate]

    shiftedPlate = []
    for line in plate:
        rocks, mem = 0, 0
        newLine = ''
        for idx, char in enumerate(line):
            if char == "O":
                rocks += 1
            if char == "#":
                newLine += "O"*rocks + (idx-mem-rocks)*"." + "#" 
                rocks = 0
                mem = idx + 1
            if idx == len(line)-1:
                newLine += "O"*rocks + (idx-mem-rocks+1)*"."
        shiftedPlate.append(newLine)
    
    if direction in ['south', 'east']:
        shiftedPlate = [line[::-1] for line in shiftedPlate]

    if direction in ['north', 'south']:
        shiftedPlate = [''.join(line) for line in zip(*shiftedPlate)]
    
    return shiftedPlate

def calculateLoad(plate):
    result = 0
    for idx, line in enumerate(plate):
        result += line.count("O")*(len(plate) - idx)
    return result

def task1():
    with open('day14.txt', 'r') as file_in:
        plate = file_in.read().splitlines()
        result = 0
        plate = tiltPlate(plate, 'north')
        result = calculateLoad(plate)
        return result
    
def task2():
    with open('day14.txt', 'r') as file_in:
        directions = ['north', 'west', 'south', 'east']
        memory = []

        plate = file_in.read().splitlines()
        for i in range(1000000000):
            direction = directions[i%4]
            plate = tiltPlate(plate, direction)
            if (str(plate), direction) in memory:
                loopStart, loopEnd = memory.index((str(plate), direction)), i
                loopLength = loopEnd - loopStart
                print(direction, "\n")
                # print(direction)
                # print(directions[loopEnd%4])
                # print(directions[loopStart%4])
                # for line in plate:
                #     print(line)
                # print(direction, "\n")
                # print(memory.index((str(plate), direction)))
                # print(memory[memory.index((str(plate), direction))])
                # for line in ["".join(list(memory[memory.index((str(plate), direction))][0]))]:
                #     print(line)
                # print(memory[memory.index((str(plate), direction))][1], "\n")
                break
            # if foundLoop and i%4 == 0:
            #     for line in plate:
            #         print(line)
            #     print()

            memory.append((str(plate), direction))

        # print(loopStart, loopEnd, loopLength)
        # print((10**9 - loopStart)%loopLength)
        # leftoverSteps = (10**9 - loopStart)%loopLength
        # stepsLeft = 10**9 - (loopStart + loopLength*((10**9 - loopStart)//loopLength))
        # print(10**9 - loopStart)
        # print((10**9 - loopStart)//loopLength)
        # print(loopLength * ((10**9 - loopStart)//loopLength))
        # print("stepsLeft", stepsLeft)
        # print("leftoverSteps", leftoverSteps)
        print("loopStart", loopStart)
        print("loopLength", loopLength)
        print(1000000000 - 1 - loopStart)
        print((1000000000 - 1 - loopStart)//loopLength)
        print(loopLength * ((1000000000 - 1 - loopStart)//loopLength))
        print(1000000000 - 1 - loopStart - loopLength * ((1000000000 - 1 - loopStart)//loopLength))
        leftoverSteps = 1000000000 - 1 - loopStart - loopLength * ((1000000000 - 1 - loopStart)//loopLength)
        for i in range(1, leftoverSteps + 1):
            direction = directions[(loopEnd + i)%4]
            print(i, direction)
            plate = tiltPlate(plate, direction)

        result = calculateLoad(plate)
        return result

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f'Task 1: {solution1}')
    solution2 = task2()
    print(f'Task 2: {solution2}')