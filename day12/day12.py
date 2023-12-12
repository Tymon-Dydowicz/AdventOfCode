import os
import time

def generateAllPossibleAsignments(springsSeries):
    if '?' not in springsSeries:
        return [springsSeries]
    else:
        return generateAllPossibleAsignments(springsSeries.replace('?', '#', 1)) + generateAllPossibleAsignments(springsSeries.replace('?', '.', 1))
    
def generateOnlyValidAsignments(springsSeries, lengths):
    numbers = [s.count('#') for s in springsSeries.split('.') if s != '']
    print(numbers, lengths)
    for i in range(len(lengths)):
        if numbers[i] > lengths[i]:
            return []
    if '?' not in springsSeries:
        return [springsSeries]
    else:
        return generateAllPossibleAsignments(springsSeries.replace('?', '#', 1)) + generateAllPossibleAsignments(springsSeries.replace('?', '.', 1))

def task1():
    with open('day12.txt', 'r') as file_in:
        lines = file_in.read().splitlines()
        result = 0
        for line in lines:
            input = line.split(' ')
            # springsSeries = [s for s in input[0].split('.') if s != '']
            springsSeries = input[0] 
            lengths = [int(i) for i in input[1].split(',')]
            possibleAsignments = generateAllPossibleAsignments(springsSeries)
            for assignment in possibleAsignments:
                numbers = [s.count('#') for s in assignment.split('.') if s != '']
                if numbers == lengths:
                    result += 1
            
            # print(springsSeries, lengths)
        return result
                

def task2():
    with open('day12.txt', 'r') as file_in:
        lines = file_in.read().splitlines()
        result = 0
        for line in lines:
            input = line.split(' ')
            # springsSeries = [s for s in input[0].split('.') if s != '']
            springsSeries = "?".join(input[0] for _ in range(5))
            lengths = [int(i) for i in input[1].split(',')] * 5
            print(springsSeries, lengths)
            possibleAsignments = generateOnlyValidAsignments(springsSeries, lengths)
            start = time.time()
            for assignment in possibleAsignments:
                numbers = [s.count('#') for s in assignment.split('.') if s != '']
                if numbers == lengths:
                    result += 1
            end = time.time()
            print(end - start)
            print(result)
            
            # print(springsSeries, lengths)
        return result

            

                

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # solution1 = task1()
    # print(f'Task 1: {solution1}')
    solution2 = task2()
    print(f'Task 2: {solution2}')