def solution(s):
    t = sorted(s)
    answer = ''.join(t[::-1])
    return answer