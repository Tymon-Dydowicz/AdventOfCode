import os

def extrapolate(sequence, direction):
    differences = [sequence]
    difference = [x1-x2 for x1, x2 in zip(sequence[1:], sequence[:-1])]
    differences.append(difference)
    while any(diff != 0 for diff in difference):
        difference = [x1-x2 for x1, x2 in zip(difference[1:], difference[:-1])]
        differences.append(difference)

    for idx, difference in enumerate(reversed(differences)):
        if direction == 'forward':
            if idx == 0:
                difference.append(0)
            else:
                difference.append(differences[len(differences)-idx][-1]+difference[-1])
        elif direction == 'backward':
            if idx == 0:
                difference.insert(0, 0)
            else:
                difference.insert(0, difference[0] - differences[len(differences)-idx][0])
    return differences[0]

def task1():
    with open('day9.txt', 'r') as file_in:
        result = 0
        for line in file_in:
            sequence = [int(x) for x in line.strip().split(" ")]
            result += extrapolate(sequence, 'forward')[-1]
        return result
    
def task2():
    with open('day9.txt', 'r') as file_in:
        result = 0
        for line in file_in:
            sequence = [int(x) for x in line.strip().split(" ")]
            result += extrapolate(sequence, 'backward')[0]
        return result
            
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f'Task 1: {solution1}')
    solution2 = task2()
    print(f'Task 2: {solution2}')