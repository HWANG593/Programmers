def solution(arr):
    answer = []
    index = []

    for i in range(len(arr)):
        if i == len(arr)-1:
            break
    
        if arr[i] == arr[i+1]:
            arr[i] = 'a'

    for j in range(len(arr)):
        if arr[j] != 'a':
            index.append(j)
        
    for k in range(len(index)):
        answer.append(arr[index[k]])
    
    return answer