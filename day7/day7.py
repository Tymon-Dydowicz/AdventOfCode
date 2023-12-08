import os
from collections import Counter
from functools import cmp_to_key

def addZToMostCommon(cardFaces):
    if len(cardFaces) > 1 and 'Z' in cardFaces:
        temp = cardFaces.pop('Z')
        cardFaces[cardFaces.most_common(1)[0][0]] += temp
    return cardFaces

def compareSameTypeHands(hand1, hand2, faceValues):
    for i in range(len(hand1)):
        if hand1[i] != hand2[i]:
            return faceValues[hand1[i]] - faceValues[hand2[i]]
    return 0

def isFullHouse(cardFaces):
    return len(cardFaces) == 2 and cardFaces.most_common(1)[0][1] == 3

def is2Pairs(cardFaces):
    return len(cardFaces) == 3 and cardFaces.most_common(1)[0][1] == 2

def compareEasyTypes(mc1, mc2, cards1, cards2, faceValues):
    for noOfSameCards in range(5, 0, -1):
        if mc1 == noOfSameCards and mc2 == noOfSameCards:
            return compareSameTypeHands(cards1, cards2, faceValues)
        elif mc1 == noOfSameCards:
            return 1
        elif mc2 == noOfSameCards:
            return -1


def compareHands(hand1, hand2):
    faceValues = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'Z':1}
    cards1, cards2 = hand1[0], hand2[0]
    cardFaces1, cardFaces2 = Counter(cards1), Counter(cards2)

    cardFaces1 = addZToMostCommon(cardFaces1)
    cardFaces2 = addZToMostCommon(cardFaces2)

    if len(cardFaces1) > len(cardFaces2):
        return -1
    elif len(cardFaces1) < len(cardFaces2):
        return 1
    
    if isFullHouse(cardFaces1) and isFullHouse(cardFaces2):
        return compareSameTypeHands(cards1, cards2, faceValues)
    
    if is2Pairs(cardFaces1) and is2Pairs(cardFaces2):
        return compareSameTypeHands(cards1, cards2, faceValues)
    
    mc1, mc2 = cardFaces1.most_common(1)[0][1], cardFaces2.most_common(1)[0][1]
    return compareEasyTypes(mc1, mc2, cards1, cards2, faceValues)

        
def task1():
    with open('day7.txt', 'r') as file_in:
        handsAndBids = []
        for line in file_in:
            handsAndBids.append(line.strip().split())
        orderedHands = sorted(handsAndBids, key=cmp_to_key(compareHands))
        return sum([int(hand[1])*(idx+1) for idx, hand in enumerate(orderedHands)])
    
def task2():
    with open('day7.txt', 'r') as file_in:
        handsAndBids = []
        for line in file_in:
            handsAndBids.append(line.replace('J', 'Z').strip().split())
        orderedHands = sorted(handsAndBids, key=cmp_to_key(compareHands))
        return sum([int(hand[1])*(idx+1) for idx, hand in enumerate(orderedHands)])



if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f"Task 1: {solution1}\n")
    solution2 = task2()
    print(f"Task 2: {solution2}\n")