def mergeMeetings(meeting):
    meeting.sort()
    result = []

    result.append(meeting[0])
    for i in range(1, len(meeting)):
        prevMeeting = result[-1]
        currMeeting = meeting[i]
        if currMeeting[0] <= prevMeeting[1]:
            result.pop()
            result.append((prevMeeting[0], max(currMeeting[1], prevMeeting[1])))
        else:
            result.append(currMeeting)
    
    return result

def solution(meetings):
    # sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

def main():
    m0 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    m1 = [(1,3), (2,4)]
    m3 = [(1,5), (2,3)]
    m4 = [(1, 10), (2, 6), (3, 5), (7, 9)]
    print(mergeMeetings(m4))
    print(solution(m4))

main()