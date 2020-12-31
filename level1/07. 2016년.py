def solution(a, b):
    if a == 1 or a == 4 or a == 7:
        if b%7 == 1:
            return 'FRI'
        elif b%7 == 2: 
            return 'SAT'
        elif b%7 == 3 :
            return 'SUN'
        elif b%7 == 4 :
            return 'MON'
        elif b%7 == 5 :
            return 'TUE'
        elif b%7 == 6 :
            return 'WED'
        elif b%7 == 0 :
            return 'THU'
        
    if a == 2 or a == 8:
        if b%7 == 1: 
            return 'MON'
        elif b%7 == 2: 
            return 'TUE'
        elif b%7 == 3 :
            return 'WED'
        elif b%7 == 4 :
            return 'THU'
        elif b%7 == 5 :
            return 'FRI'
        elif b%7 == 6 :
            return 'SAT'
        elif b%7 == 0 :
            return 'SUN'
        
    if a == 3 or a == 11:
        if b%7 == 1 :
            return 'TUE'
        elif b%7 == 2 :
            return 'WED'
        elif b%7 == 3 :
            return 'THU'
        elif b%7 == 4 :
            return 'FRI'
        elif b%7 == 5 :
            return 'SAT'
        elif b%7 == 6 :
            return 'SUN'
        elif b%7 == 0 :
            return 'MON'
    
    if a == 5 :
        if b%7 == 1 :
            return 'SUN'
        elif b%7 == 2 :
            return 'MON'
        elif b%7 == 3 :
            return 'TUE'
        elif b%7 == 4 :
            return 'WED'
        elif b%7 == 5 :
            return 'THU'
        elif b%7 == 6 :
            return 'FRI'
        elif b%7 == 0 :
            return 'SAT'

    if a == 6 :
        if b%7 == 1 :
            return 'WED'
        elif b%7 == 2 :
            return 'THU'
        elif b%7 == 3 :
            return 'FRI'
        elif b%7 == 4 :
            return 'SAT'
        elif b%7 == 5 :
            return 'SUN'
        elif b%7 == 6 :
            return 'MON'
        elif b%7 == 0 :
            return 'TUE'
        
    if a == 9 or a == 12:
        if b%7 == 1 :
            return 'THU'
        elif b%7 == 2 :
            return 'FRI'
        elif b%7 == 3 :
            return 'SAT'
        elif b%7 == 4 :
            return 'SUN'
        elif b%7 == 5 :
            return 'MON'
        elif b%7 == 6 :
            return 'TUE'
        elif b%7 == 0 :
            return 'WED'
        
    if a == 10 :
        if b%7 == 1 :
            return 'SAT'
        elif b%7 == 2 :
            return 'SUN'
        elif b%7 == 3 :
            return 'MON'
        elif b%7 == 4 :
            return 'TUE'
        elif b%7 == 5 :
            return 'WED'
        elif b%7 == 6 :
            return 'THU'
        elif b%7 == 0 :
            return 'FRI'