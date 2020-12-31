def solution(participant, completion):
    a = participant
    b = completion
    a.sort()
    b.sort()
    
    for i in range(len(b)):
        
            if b[i]!=a[i]:
                return a[i]
    return a[-1]