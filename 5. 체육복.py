def solution(n, lost, reserve):
    answer = 0
    
    cloth = [1]*n

    for i in range(len(lost)):
        cloth[lost[i]-1] = cloth[lost[i]-1]-1
        
    for j in range(len(reserve)):
        cloth[reserve[j]-1] = cloth[reserve[j]-1]+1
    
    
    for i in range(len(cloth)):
        if i == 0:
            if cloth[i]==2 :
                if cloth[i+1]==0:
                    cloth[i]=1
                    cloth[i+1]=1
                    
                
            
        elif i == len(cloth)-1:
            if cloth[i] == 2:
                if cloth[i-1] ==0:
                    cloth[i-1] = 1
                    cloth[i] = 1
        
        elif cloth[i]==2:
            if cloth[i-1]==0:
                cloth[i-1]=1
                cloth[i] = 1
            else:
                if cloth[i+1]==0:
                    cloth[i+1] = 1
                    cloth[i] = 1
            
    answer = cloth.count(1) + cloth.count(2)
    
    return answer