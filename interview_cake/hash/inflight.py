def inflight(flight_length, movie_lengths):
    sumOther = set()
    for i in movie_lengths:
        result = flight_length - i
        if i in sumOther:
            return True
        sumOther.add(result)
        print(sumOther)


    return False

def inflightAmazon(d, movieDurations):
    pass

def main():
    moveDurations = [60, 120, 150, 30]
    flightDuration = 90
    print(inflight(flightDuration, moveDurations))

main()

'''
Followup:
2. What if we wanted to fill the flight length as nicely as possible with any number of movies (not just 2)? DP?
'''