def solution(people, limit):
    answer = 0
    people.sort()
    light = 0
    heavy = len(people) - 1
    cnt = 0

    while(light < heavy):
        if(people[light] + people[heavy] <= limit):
            cnt += 1
            light += 1
            heavy -= 1
        else:
            heavy -= 1

    answer = len(people) - cnt

    return answer