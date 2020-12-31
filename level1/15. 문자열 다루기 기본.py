def solution(s):
    count = 0
    if len(s) == 4 or len(s) == 6:
        
        for i in range(len(s)):
            if s[i].isalpha()==True:
                count += 1
                break
    else: 
        return len(s) == 4 or len(s) == 6

    
    return count==0
            