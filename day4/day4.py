import os

def task1():
    with open('day4.txt', 'r') as file_in:
        scores = {}
        noOfCopies = {}
        for idx, line in enumerate(file_in):
            noOfCopies.setdefault(idx, 0)
            noOfCopies[idx] += 1
            scores[idx] = 0
            numbers = line.strip('\n').split(':')[1].split('|')
            winningNumbers, yourNumbers = numbers
            winning = set([num for num in winningNumbers.split(' ')])
            your = set([num for num in yourNumbers.split(' ')])
            noOfCoveredNumbers = len(winning.intersection(your)) - 1
            if noOfCoveredNumbers > 0:  
                scores[idx] = 2**(noOfCoveredNumbers - 1)
                for surplus in range(noOfCoveredNumbers):
                    noOfCopies.setdefault(idx+surplus+1, 0)
                    noOfCopies[idx+surplus+1] += noOfCopies[idx]

        noOfCards = sum(noOfCopies.values())
        sumOfScores = sum(scores.values())
        return sumOfScores, noOfCards


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1, solution2 = task1()
    print(f"Solution to part 1: {solution1}")
    print(f"Solution to part 2: {solution2}")
