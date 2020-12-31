def solution(arr1, arr2):
    arr3 = []
    for row in range(len(arr1)):
        tmp = []
        for col in range(len(arr1[0])):
            tmp.append(arr1[row][col] + arr2[row][col])
        arr3.append(tmp)
    return arr3