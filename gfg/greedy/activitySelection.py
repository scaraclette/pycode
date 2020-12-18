'''
    Activity Selection Problem
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
'''

def activitySelection(start, finish):
    intervals = []
    result = []
    for i in range(len(start)):
        intervals.append((start[i], finish[i]))

    print(intervals)

    result = []
    

def main():
    start = [10,12,20]
    finish = [20,25,30]