def solution(n):
    if n % 2 == 1:
        a = '수' + '박수'*(n//2)
        answer = a
    else:
        a = '수박'*(n//2)
        answer = a
    
    return answer