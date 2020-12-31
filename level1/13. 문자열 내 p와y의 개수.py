def solution(s):
    count_p = 0
    count_y = 0
    t = s.lower()
    
    for i in range(len(t)):
        if t[i] == 'p':
            count_p += 1
        elif t[i] == 'y':
            count_y += 1
    
    return count_p == count_y