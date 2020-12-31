def solution(phone_number):
    end = phone_number[len(phone_number)-4:]
    
    front = '*'*(len(phone_number)-4)
    
    answer = front+end
    
    return answer