def solution(n):

    list = []

    for i in range(11):
        if n<10**i:     #i는 3이되겠지
            t = i
            break
    
    
    for i in range(t):
        a = n//(10**(t-1-i))
    
        n = n - n//(10**(t-1-i)) * (10**(t-1-i))
    
        list.append(a)
        answer = list[::-1]
    
    return answer