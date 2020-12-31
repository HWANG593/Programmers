def solution(n):
    N = str(n)
        
    list = []
    for i in range(len(N)):
        list.append(N[i])
        
    list.sort()
    answer = ''.join(list[::-1])
    answer_int = int(answer)
    return answer_int