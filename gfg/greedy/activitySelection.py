'''
    Activity Selection Problem
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
'''

def activitySelection(start, finish):
    intervals = []
    result = []
    for i in range(len(start)):
        intervals.append((start[i], finish[i]))

    indexDict = {i: x for x, i in enumerate(intervals)}
    print(indexDict[(1,2)])

    print(indexDict)

    result = [intervals[0]]
    for i in range(1, len(intervals)):
        prevFinish = result[-1][1]
        currentStart = intervals[i][0]
        if currentStart >= prevFinish:
            result.append(intervals[i])
    
    for i in result:
        print(indexDict[i])

def main():
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    activitySelection(start, finish)

main()