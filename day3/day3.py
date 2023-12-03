import os

def extractNumber(line, column, direction):
    number = line[column]
    pointer = column + direction
    while line[pointer].isdigit():
        number += line[pointer]
        pointer += direction
    return number[::-1] if direction == -1 else number

def extractNumbersFromDifferentLine(line, column):
    Left = Right = ""
    if line[column-1].isdigit():
        Left = extractNumber(line, column-1, -1)
    if line[column+1].isdigit():
        Right = extractNumber(line, column+1, 1)
    return [int(num) for num in (Left+line[column]+Right).split(".") if num.isnumeric()]

def task1():
    with open('day3.txt', 'r') as file_in:
        lines = file_in.readlines()
        task2Result = 0
        task1Result = 0
        for row, line in enumerate(lines):
            for col, char in enumerate(line.strip('\n')):
                if not char.isdigit() and char != '.':
                    numbers = []
                                    
                    if line[col-1].isdigit():
                        numbers.append(int(extractNumber(line, col-1, -1)))
                    if line[col+1].isdigit():
                        numbers.append(int(extractNumber(line, col+1, 1)))

                    numbers.extend(extractNumbersFromDifferentLine(lines[row-1], col))
                    numbers.extend(extractNumbersFromDifferentLine(lines[row+1], col))

                    if len(numbers) == 2:
                        task2Result += numbers[0] * numbers[1]
                    task1Result += sum(numbers)
                    
        return task1Result, task2Result


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1, solution2 = task1()
    print(f"Solution to part 1: {solution1}")
    print(f"Solution to part 2: {solution2}")