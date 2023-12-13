import os

def countPattern(pattern):
    sumOfIndicies = 0
    for idx in range(len(pattern[:-1])):
        counter = 0
        broken = False
        while idx - counter >= 0 and idx + counter + 1 < len(pattern):
            if pattern[idx - counter] != pattern[idx + counter + 1]:
                broken = True
                break
            counter += 1
        if not broken:
            sumOfIndicies += (idx+1)

    return sumOfIndicies

def fixSmudge(pattern):
    smudge = None
    mem = None
    for idx1 in range(len(pattern[:-1])):
        counter = 0
        broken = False
        while idx1 - counter >= 0 and idx1 + counter + 1 < len(pattern):
            for idx2 in range(len(pattern[idx1 - counter])):
                if pattern[idx1 - counter][idx2] != pattern[idx1 + counter + 1][idx2]:
                    if smudge is not None:
                        broken = True
                        smudge, mem = None, None
                        break
                    smudge = (idx1 - counter, idx2)
                    mem = idx1

            if broken:
                break
            counter += 1
        if smudge is not None:
            break

    if not broken and smudge is not None:
        change = "#" if pattern[smudge[0]][smudge[1]] == "." else "."
        pattern[smudge[0]] = pattern[smudge[0]][:smudge[1]] + change + pattern[smudge[0]][smudge[1]+1:]

    return pattern, mem
    


def task1():
    with open('day13.txt', 'r') as file_in:
        patterns = []
        result = 0

        temp = []
        for line in file_in:
            if line == '\n':
                patterns.append(temp)
                temp = []
                continue
            line = line.strip()
            temp.append(line)
        patterns.append(temp)

        transposedPatterns = [[''.join(line) for line in zip(*pattern)] for pattern in patterns]
        
        for pattern in patterns:
            result += countPattern(pattern)*100
        
        for pattern in transposedPatterns:
            result += countPattern(pattern)

        return result
        
def task2():
    with open('day13.txt', 'r') as file_in:
        patterns = []
        result = 0

        temp = []
        for line in file_in:
            if line == '\n':
                patterns.append(temp)
                temp = []
                continue
            line = line.strip()
            temp.append(line)
        patterns.append(temp)



        transposedPatterns = [[''.join(line) for line in zip(*pattern)] for pattern in patterns]

        for pattern in patterns:
            pattern, idx = fixSmudge(pattern)
            if idx is not None:
                result += (idx+1)*100
        
        for pattern in transposedPatterns:
            pattern, idx = fixSmudge(pattern)
            if idx is not None:
                result += (idx+1)

        return result

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f'Task 1: {solution1}')
    solution2 = task2()
    print(f'Task 2: {solution2}')