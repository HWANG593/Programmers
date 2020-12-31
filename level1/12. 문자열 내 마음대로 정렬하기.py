
def solution(strings, n):
    
    answer = sorted(strings, key = lambda t:(t[n],t))
    return answer