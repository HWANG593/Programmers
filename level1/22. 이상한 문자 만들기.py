def solution(s):
    
    a = s.split(' ')

    list = []
    index = []

    for i in range(len(s)):
        if s[i] == ' ':
            index.append(i)

    for i in range(len(a)):
        for j in range(len(a[i])):
            if j%2 != 1:
                list.append(a[i][j].upper())
            else:
                list.append(a[i][j].lower())

    for i in range(len(index)):
        list.insert(index[i],' ')

    answer = ''.join(list)
    return answer