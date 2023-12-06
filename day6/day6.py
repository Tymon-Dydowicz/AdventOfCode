import os
from math import floor, ceil
import time

def task1():
    with open('day6.txt', 'r') as file_in:
        lines = file_in.readlines()
        times = [int(time) for time in lines[0][5:].strip().split()]
        distances = [int(dist) for dist in lines[1][9:].strip().split()]
        result = 1

        for time, distance in zip(times, distances):
            raceRecords = 0
            lower, upper = floor(time/2), ceil(time/2)

            if time % 2 == 0:
                raceRecords -= 1

            while lower * upper > distance:
                raceRecords += 2
                lower -= 1
                upper += 1
            
            result *= raceRecords
                
        return result
    
def task2():
    with open('day6.txt', 'r') as file_in:
        lines = file_in.readlines()
        time = int("".join(lines[0][5:].strip().split()))
        distance = int("".join(lines[1][9:].strip().split()))
        raceRecord = 0
        lower, upper = floor(time/2), ceil(time/2)

        if time % 2 == 0:
            raceRecord -= 1

        while lower * upper > distance:
            raceRecord += 2
            lower -= 1
            upper += 1
        
        return raceRecord
    
def task2Fast():
    with open('day6.txt', 'r') as file_in:
        lines = file_in.readlines()
        time = int("".join(lines[0][5:].strip().split()))
        distance = int("".join(lines[1][9:].strip().split()))
        delta = time**2 - 4*distance
        x1 = (time + delta**0.5)/2
        x2 = (time - delta**0.5)/2
        return(int(x1) - int(x2))



if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f"Task 1: {solution1}\n")
    start = time.time()
    solution2 = task2()
    end = time.time()
    print(f"Task 2: {solution2}")
    print(f"Time: {end - start} seconds\n")
    start = time.time()
    solution2Fast = task2Fast()
    end = time.time()
    print(f"Task 2 (fast): {solution2Fast}")
    print(f"Time: {end - start} seconds")