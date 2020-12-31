def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        a = array[commands[i][0]-1 : commands[i][1]] # 2-1 부터 5까지 index 1 은 포함 5는 포함 x
        a.sort()
        answer.append(a[commands[i][2]-1]) # 3번째 수는 index 2번에 해당함
    
    return answer