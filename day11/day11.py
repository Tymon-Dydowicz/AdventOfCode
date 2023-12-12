import os

def task(expansionRate):
    with open('day11.txt', 'r') as file_in:
        galaxies, result = [], 0

        lines = file_in.read().splitlines()
        expandedRows, expandedCols = [i for i in range(len(lines))], [i for i in range(len(lines[0]))]
        
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "#":
                    galaxies.append((row, col))

        for galaxy in galaxies:
            if galaxy[0] in expandedRows:
                expandedRows.remove(galaxy[0])
            if galaxy[1] in expandedCols:
                expandedCols.remove(galaxy[1])

        for idx, galaxy1 in enumerate(galaxies):
            for galaxy2 in galaxies[idx+1:]:
                for row in expandedRows:
                    if galaxy1[0] < row < galaxy2[0] or galaxy2[0] < row < galaxy1[0]:
                        result += expansionRate
                for col in expandedCols:
                    if galaxy1[1] < col < galaxy2[1] or galaxy2[1] < col < galaxy1[1]:
                        result += expansionRate
                result += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

        return result
                




if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task(1)
    print(f'Task 1: {solution1}')
    solution2 = task(999_999)
    print(f'Task 2: {solution2}')