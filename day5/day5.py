import os
import time

def goThroughMaps(seed, maps):
    for map in maps.values():
        for mapping in map:
            dest, source, length = mapping
            diff = dest - source
            if seed in range(source, source+length):
                seed = seed + diff
                break
    return seed

def goThroughMapsWithRange(seedRange, maps):
    sameRanges = [seedRange]
    alteredRanges = []
    for map in maps.values():
        while sameRanges:
            testedSeedRange = sameRanges.pop(0)
            found = False
            for mapping in map:
                dest, source, length = mapping
                diff = dest - source
                seedLower = testedSeedRange[0]
                seedUpper = testedSeedRange[0] + testedSeedRange[1]
                if seedLower >= source + length or seedUpper <= source: #Case 1_1 1_2
                    continue
                
                if seedLower < source and seedUpper > source and seedUpper <= source + length: #Case 2_1
                    seedRangeS1 = (seedLower, testedSeedRange[1] - (seedUpper - source))
                    seedRangeA1 = (source + diff, (seedUpper - source))

                    sameRanges.append(seedRangeS1)
                    alteredRanges.append(seedRangeA1)
                    found = True
                    break
                
                if source <= seedLower < source + length and seedUpper > source + length: #Case 2_2
                    seedRangeS1 = (source + length, testedSeedRange[1] - (source + length - seedLower))
                    seedRangeA1 = (seedLower + diff, (source + length - seedLower))

                    sameRanges.append(seedRangeS1)
                    alteredRanges.append(seedRangeA1)
                    found = True
                    break

                if seedLower < source and seedUpper > source + length: #Case 3
                    seedRangeS1 = (seedLower, source - seedLower)
                    seedRangeA1 = (source + diff, length)
                    seedRangeS2 = (source + length, seedUpper - (source + length))

                    sameRanges.append(seedRangeS1)
                    sameRanges.append(seedRangeS2)
                    alteredRanges.append(seedRangeA1)
                    found = True
                    break

                if seedLower >= source and seedUpper <= source + length: #Case 4
                    seedRangeA1 = (seedLower + diff, testedSeedRange[1])

                    alteredRanges.append(seedRangeA1)
                    found = True
                    break

            if not found:
                alteredRanges.append(testedSeedRange)

        sameRanges = alteredRanges
        alteredRanges = []
    return min(range[0] for range in sameRanges)
        
def task1():
    with open('day5.txt', 'r') as file_in:
        lines = file_in.readlines()
        seeds = [int(seed) for seed in lines.pop(0).strip('\n').split(' ')[1:]]
        maps = {}
        idx, mapIndex = 0, 0

        while idx < len(lines):
            line = lines[idx]
            if line == '\n':
                mapIndex += 1
                idx += 1
            else:
                mapping = [int(i) for i in line.strip('\n').split(' ')]
                maps.setdefault(mapIndex, []).append(mapping)
            idx += 1

        location = float("inf")
        for seed in seeds:
            location = min(location, goThroughMaps(seed, maps))
        return location

def task2():
    with open('day5.txt', 'r') as file_in:
        lines = file_in.readlines()
        seedRanges = [int(seed) for seed in lines.pop(0).strip('\n').split(' ')[1:]]
        seedRanges = [(start, length) for start, length in zip(seedRanges[::2], seedRanges[1::2])]
        maps = {}
        idx, mapIndex = 0, 0
        
        while idx < len(lines):
            line = lines[idx]
            if line == '\n':
                mapIndex += 1
                idx += 1
            else:
                mapping = [int(i) for i in line.strip('\n').split(' ')]
                maps.setdefault(mapIndex, []).append(mapping)
            idx += 1
        
        location = float("inf")
        for seedRange in seedRanges:
            location = min(location, goThroughMapsWithRange(seedRange, maps))
        return location
                

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    solution1 = task1()
    print(f"Task 1: {solution1}")
    start = time.time()
    solution2 = task2()
    end = time.time()
    print(f"Task 2: {solution2}")
    print(f"Time: {end - start}")