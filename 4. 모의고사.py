def solution(answers):

    
    s1 = [1,2,3,4,5]*2000
    s2 = [2,1,2,3,2,4,2,5]*1250
    s3 = [3,3,1,1,2,2,4,4,5,5]*1000
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        
        if answers[i]==s1[i]:
            count1+=1
        if answers[i]==s2[i]:
            count2+=1
        if answers[i]==s3[i]:
            count3+=1
    
    
    if count1>count2 and count1>count3:
        return [1]
    
    if count2>count1 and count2>count3:
        return [2]
    
    if count3>count1 and count3>count2:
        return [3]
    
    if count1==count2 and count1>count3:
        return [1,2]
    
    if count1==count3 and count1 > count2:
        return [1,3]
    
    if count2==count3 and count2 > count1:
        return [2,3]
    
    if count2==count3 and count2 == count1:
        return [1,2,3]