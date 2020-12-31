
def solution(a, b):
    list = []
    answer = 0
    count1 = 0
    count2 = 0
    
    if b>a:
        for i in range(10000000000):
            if a+i != b:
                list.append(a+i)
            
            else:
                list.append(b)
                break
        return sum(list)
                    
    if b<a:
        for i in range(10000000000):
            if a-i != b:
                list.append(a-i)
            
            else:
                list.append(b)
                break
        return sum(list)
    if a==b:
        return a