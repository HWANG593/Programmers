def solution(num):
    for i in range(500):
        if num == 1:
            result = i
            break
        elif num%2 == 0:
            num  = num/2
        
        elif num%2 != 0:
            num = num*3+1
            
    if num != 1:
        result = -1 
    return result