import os

def HASH(string):
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    return current


def task1():
    with open('day15.txt', 'r') as file_in:
        instructions = file_in.read().splitlines()[0].split(',')
        hashes = [HASH(x) for x in instructions]
        return sum(hashes)
    
def task2():
    with open('day15.txt', 'r') as file_in:
        instructions = file_in.read().splitlines()[0].split(',')
        hashes = [HASH(x[:-2]) for x in instructions]
        print(hashes)
        return sum(hashes)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # solution1 = task1()
    # print(f'Task 1: {solution1}')
    solution2 = task2()
    print(f'Task 2: {solution2}')