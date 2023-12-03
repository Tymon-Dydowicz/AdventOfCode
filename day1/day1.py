import os

def task1():
    with open('day1.txt') as file_in:
        numbers = []
        for line in file_in:
            numbersInLine = ''.join(filter(str.isdigit, line))
            numbers.append(int(numbersInLine[0] + numbersInLine[-1]))

        return sum(numbers)


def task2():
    with open('day1.txt') as file_in:
        numbers = []
        for line in file_in:
            line = line.replace('one', "one1one")
            line = line.replace('two', "two2two")
            line = line.replace('three', "three3three")
            line = line.replace('four', "four4four")
            line = line.replace('five', "five5five")
            line = line.replace('six', "six6six")
            line = line.replace('seven', "seven7seven")
            line = line.replace('eight', "eight8eight")
            line = line.replace('nine', "nine9nine")
            line = line.replace('zero', "zero0zero")

            numbersInLine = ''.join(filter(str.isdigit, line))
            numbers.append(int(numbersInLine[0] + numbersInLine[-1]))
        return sum(numbers)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    solution1 = task1()
    print(solution1)
    solution2 = task2()
    print(solution2)