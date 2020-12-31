import math

def distance(x1, y1, x2, y2):
    dist = abs(x1-x2) + abs(y1 - y2) 
    return dist

def solution(numbers, hand):
    result = []
    LP = (1,1)
    RP = (3,1)
    
    for i in range(len(numbers)):
        if numbers[i] == 1 :
            result.append('L')
            LP = (1,4)
        
        elif numbers[i] == 4 :
            result.append('L')
            LP = (1,3)
    
        elif numbers[i] == 7 :
            result.append('L')
            LP = (1,2)
            
        elif numbers[i] == 3 :
            result.append('R')
            RP = (3,4)
        
        elif numbers[i] == 6 :
            result.append('R')
            RP = (3,3)
    
        elif numbers[i] == 9 :
            result.append('R')
            RP= (3,2)
        
        
        elif numbers[i] == 2:
            if distance(LP[0],LP[1],2,4) > distance(RP[0],RP[1],2,4):
                result.append('R')
                RP = (2,4)
            elif distance(LP[0],LP[1],2,4) < distance(RP[0],RP[1],2,4):
                result.append('L')
                LP = (2,4)
            elif  distance(LP[0],LP[1],2,4) == distance(RP[0],RP[1],2,4):
                result.append(hand[0].upper())
                if hand == 'right':
                    RP = (2,4)
                elif hand == 'left':
                    LP = (2,4)
                    
        elif numbers[i] == 5:
            if distance(LP[0],LP[1],2,3) > distance(RP[0],RP[1],2,3):
                result.append('R')
                RP = (2,3)
            elif distance(LP[0],LP[1],2,3) < distance(RP[0],RP[1],2,3):
                result.append('L')
                LP = (2,3)
            elif  distance(LP[0],LP[1],2,3) == distance(RP[0],RP[1],2,3):
                result.append(hand[0].upper())
                if hand == 'right':
                    RP = (2,3)
                elif hand == 'left':
                    LP = (2,3)
            
        elif numbers[i] == 8:
            if distance(LP[0],LP[1],2,2) > distance(RP[0],RP[1],2,2):
                result.append('R')
                RP = (2,2)
            elif distance(LP[0],LP[1],2,2) < distance(RP[0],RP[1],2,2):
                result.append('L')
                LP = (2,2)
            elif  distance(LP[0],LP[1],2,2) == distance(RP[0],RP[1],2,2):
                result.append(hand[0].upper())
                if hand == 'right':
                    RP = (2,2)
                elif hand == 'left':
                    LP = (2,2)
                    
        elif numbers[i] == 0:
            if distance(LP[0],LP[1],2,1) > distance(RP[0],RP[1],2,1):
                result.append('R')
                RP = (2,1)
            elif distance(LP[0],LP[1],2,1) < distance(RP[0],RP[1],2,1):
                result.append('L')
                LP = (2,1)
            elif  distance(LP[0],LP[1],2,1) == distance(RP[0],RP[1],2,1):
                result.append(hand[0].upper())
                if hand == 'right':
                    RP = (2,1)
                elif hand == 'left':
                    LP = (2,1)
                
    answer = ''.join(result)
    return answer