def solution(board, moves):
    answer = 0
    basket = []
    for i in range(len(moves)):
        col = moves[i]-1
        for row in range(len(board)):
            if board[row][col]!=0:
                basket.append(board[row][col])
                board[row][col]=0
                answer+=inspect(basket)
                print(answer)
                break
    return answer

def inspect(b):
    if len(b) < 2:
        return 0
    else: 
        last = b[len(b)-1]
        pre_last = b[len(b)-2]
        if last == pre_last:
            b.pop()
            b.pop()
            return 2
        else:
            return 0