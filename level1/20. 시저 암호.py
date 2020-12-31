from string import ascii_lowercase
from string import ascii_uppercase


alpha_list = list(ascii_lowercase)
ALPHA_LIST = list(ascii_uppercase)

def solution(s, n):
    mod = []

    for i in range(len(s)):
        for j in range(len(alpha_list)):
            if s[i] == alpha_list[j]:
                if (j+n) > 25:
                    mod.append(alpha_list[j+n-26])
                else:
                    mod.append(alpha_list[j+n])
        
            elif s[i] == ALPHA_LIST[j]:
                if (j+n) >25:
                    mod.append(ALPHA_LIST[j+n-26])
            
                else:
                    mod.append(ALPHA_LIST[j+n])
            elif s[i] == ' ':
                mod.append(' ')
                break
    answer = ''.join(mod)
    return answer