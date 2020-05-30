def solution(n, lost, reserve):
    temp = list(set(lost + reserve))
    answer = n - len(temp)
    temp = []

    for i in lost:
        if(i in reserve):
            answer += 1
            reserve.remove(i)
            temp.append(i)
    
    lost = list(set(lost) - set(temp))
    
    for i in lost:
        if(i-1 in reserve):
            answer += 2
            reserve.remove(i-1)
        elif(i+1 in reserve):
            answer += 2
            reserve.remove(i+1)

    answer += len(reserve)

    return answer