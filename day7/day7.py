import os
from collections import Counter
from functools import cmp_to_key

def addZToMostCommon(cardFaces):
    if len(cardFaces) == 1:
        return cardFaces
    temp = cardFaces.pop('Z')
    cardFaces[cardFaces.most_common(1)[0][0]] += temp
    return cardFaces

def compareHands(hand1, hand2):
    faceValues = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'Z':1}
    cards1, cards2 = hand1[0], hand2[0]
    cardFaces1, cardFaces2 = Counter(cards1), Counter(cards2)
    
    # if ('Z' in cardFaces1.keys() or 'Z' in cardFaces2.keys()) and (len(cardFaces1) == 1 or len(cardFaces2) == 1):
    #     print(cardFaces1, cardFaces2)
    #     cardFaces1 = addZToMostCommon(cardFaces1)
    #     cardFaces2 = addZToMostCommon(cardFaces2)
    #     print(cardFaces1, cardFaces2)
    #     print(cards1, cards2)
    #     print("_____________________________")

    if "Z" in cardFaces1.keys():
        cardFaces1 = addZToMostCommon(cardFaces1)
    if "Z" in cardFaces2.keys():
        cardFaces2 = addZToMostCommon(cardFaces2)


    if len(cardFaces1) > len(cardFaces2):
        return -1
    elif len(cardFaces1) < len(cardFaces2):
        return 1
    else:
        mc1, mc2 = cardFaces1.most_common(1)[0][1], cardFaces2.most_common(1)[0][1]
        if mc1 == 5 and mc2 == 5:
            return faceValues[cards1[0]] - faceValues[cards2[0]]
        elif mc1 == 5:
            return 1
        elif mc2 == 5:
            return -1
        
        if mc1 == 4 and mc2 == 4:
            for i in range(len(cards1)):
                if cards1[i] != cards2[i]:
                    return faceValues[cards1[i]] - faceValues[cards2[i]]
        elif mc1 == 4:
            return 1
        elif mc2 == 4:
            return -1
        
        if (mc1 == 3 and len(cardFaces1) == 2) and (mc2 == 3 and len(cardFaces2) == 2):
            for i in range(len(cards1)):
                if cards1[i] != cards2[i]:
                    return faceValues[cards1[i]] - faceValues[cards2[i]]
        elif mc1 == 3 and len(cardFaces1) == 2:
            return 1
        elif mc2 == 3 and len(cardFaces2) == 2:
            return -1
        
        if mc1 == 3 and mc2 == 3:
            for i in range(len(cards1)):
                if cards1[i] != cards2[i]:
                    return faceValues[cards1[i]] - faceValues[cards2[i]]
        elif mc1 == 3:
            return 1
        elif mc2 == 3:
            return -1
        
        if (mc1 == 2 and len(cardFaces1) == 3) and (mc2 == 2 and len(cardFaces2) == 3):
            for i in range(len(cards1)):
                if cards1[i] != cards2[i]:
                    return faceValues[cards1[i]] - faceValues[cards2[i]]
        elif mc1 == 2 and len(cardFaces1) == 3:
            return 1
        elif mc2 == 2 and len(cardFaces2) == 3:
            return -1
        
        if mc1 == 2 and mc2 == 2:
            for i in range(len(cards1)):
                if cards1[i] != cards2[i]:
                    return faceValues[cards1[i]] - faceValues[cards2[i]]
        elif mc1 == 2:
            return 1
        elif mc2 == 2:
            return -1
        
        if mc1 == 1 and mc2 == 1:
            for i in range(len(cards1)):
                if cards1[i] != cards2[i]:
                    return faceValues[cards1[i]] - faceValues[cards2[i]]
        
        
        




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
        # print(handsAndBids)
        # print(handsAndBids[4], handsAndBids[5])
        # compareHands(handsAndBids[4], handsAndBids[5])
        orderedHands = sorted(handsAndBids, key=cmp_to_key(compareHands))
        return sum([int(hand[1])*(idx+1) for idx, hand in enumerate(orderedHands)])



if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f"Task 1: {solution1}\n")
    solution2 = task2()
    print(f"Task 2: {solution2}\n")