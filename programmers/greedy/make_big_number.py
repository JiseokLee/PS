def solution(number, k):
    answer = ''
    length = len(number)

    if (len(number) <= k):
        answer = '0'
        return answer
    
    j = 0
    for cnt in range(k):
        for i in range(j, len(number)-1):
            if(number[i] < number[i+1]):
                number = number[:i] + number[i+1:]
                if(i > 0):
                    j = i - 1
                break

    number = number[:length-k]
    answer = number

    return answer