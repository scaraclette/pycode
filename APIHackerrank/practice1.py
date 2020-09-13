import requests, pprint

def getTotalPages(team, year):
    link = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + team + '&page=1'
    req = requests.get(link).json()
    totalPages = req.get('total_pages')
    print('TOTAL PAGES:', totalPages)
    return totalPages

def getTotalGoals(team, year):
    totalPages = getTotalPages(team, year)
    otherTeam = set([])
    currentGoal = 0

    for i in range(1, totalPages+1):
        print('I:', i)
        link = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + team + '&page=' + str(i)
        req = requests.get(link).json()
        # pprint.pprint(req)
        data = req.get('data')
        for j in range(len(data)):
            currentData = data[j]
            team2 = currentData.get('team2')
            homeGoal = currentData.get('team1goals')
            otherTeam.add(team2)
            currentGoal += int(homeGoal)
        
    print('current teams:', otherTeam)
    print('current goal:', currentGoal)

    for other in otherTeam:
        totalPages = getTotalPages(other, year)
        print('otherTeam:', other, ' totalPages:', totalPages)

        for i in range(1, totalPages+1):
            link = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + other + '&page=' + str(i)
            req = requests.get(link).json()

            data = req.get('data')
            for j in range(len(data)):
                currentData = data[j]
                team2 = currentData.get('team2')
                if (team2 == team):
                    team2Goals = currentData.get('team2goals')
                    currentGoal += int(team2Goals)
    
    return currentGoal




totalGoals = getTotalGoals('Barcelona', 2011)
print(totalGoals)