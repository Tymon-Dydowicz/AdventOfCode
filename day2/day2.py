import os

def task1():
    with open('day2.txt') as file_in:
        possGames = 0
        lims = {'red' : 12, 'green' : 13, 'blue' : 14}
        for line in file_in:
            line = line.strip('\n')
            game_id, rounds = line.split(': ')
            game_id = game_id[5:]
            broken = False
            for round in rounds.split('; '):
                for pull in round.split(', '):
                    num, color = pull.split(" ")
                    if lims[color] < int(num):
                        broken = True
                        break
            if broken:
                continue
            possGames += int(game_id)
        return possGames

def task2():
    with open('day2.txt') as file_in:
        maxNum = 0
        for line in file_in:
            line = line.strip('\n')
            _, rounds = line.split(": ")
            maxes = {'red': 0, 'green': 0, 'blue': 0}
            for round in rounds.split("; "):
                for pull in round.split(", "):
                    num, color = pull.split(" ")
                    if maxes[color] < int(num):
                        maxes[color] = int(num)
            temp = 1
            for value in maxes.values():
                temp *= value
            maxNum += temp
        return maxNum
    
if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
  
    solution1 = task1()
    print(solution1)
    solution2 = task2()
    print(solution2)