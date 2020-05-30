def solution(n, costs):
    answer = 0
    dictCosts = {}
    costs.sort(key = lambda x: x[2])

    for i in range(n):
        dictCosts[i] = i

    # answer += costs[0][2]
    # dictCosts[costs[0][0]] = -1
    # dictCosts[costs[0][1]] = -1
    # n -= 1

    for n1, n2, cost in costs:
        if(n == 0):
            break
        if(dictCosts[n1] == dictCosts[n2]):
            pass

        answer += cost
        if(dictCosts[n1] > dictCosts[n2]):
            dictCosts[n1] = dictCosts[n2]
        else:
            dictCosts[n2] = dictCosts[n1]
        
        n -= 1
        

    return answer

print(solution(7, [[0,6,12],[0,3,28],[0,1,67],[0,4,17],[1,3,24],[1,4,62],[2,4,20],[2,5,37],[3,6,13],[4,5,45],[4,6,73]]))