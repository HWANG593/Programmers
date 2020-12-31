def solution(n):
    
    count = 0 
    for i in range(n):
        if n%(i+1) == 0:
            count = count + (i+1)
            

    answer = count
    return answer