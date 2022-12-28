import random

class game:
    def __init__(self):
        self.board = [[0 for i in range(3)] for i in range(3)]
        self.cnt = 0

    def over(self):
        return self.cnt == 9 or game.check(self.board) != 0

    @staticmethod
    def hash(board):
        hash, cnt = 0, 1
        for i in range(3):
            for j in range(3):
                hash += board[i][j] * cnt
                cnt *= 3
            return hash

    @staticmethod
    def check(board):
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] == 1:
            return -10
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == 1:
            return -10
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] == 1:
                return -10
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] == 1:
                return -10

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] == 2:
            return 10
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == 2:
            return 10
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] == 2:
                return 10
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] == 2:
                return 10
        return 0
    
    @staticmethod
    def solve(board, moves, turn):
        if moves == 10 or game.check(board) != 0:
            return game.check(board)
        if turn == 1:
            minVal = 1000000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = 1
                        minVal = min(game.solve(board, moves+1, 2), minVal)
                        board[i][j] = 0
            return minVal
        else:
            maxVal = -1000000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = 2
                        maxVal = max(game.solve(board, moves+1, 1), maxVal)
                        board[i][j] = 0
            return maxVal
        
    def user(self, r, c):
        self.cnt+=1
        self.board[r][c] = 1

    def comp(self):
        self.cnt+=1
        if self.cnt == 1:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            self.board[x][y] = 2
            return x,y
        
        best,x,y = -2e9, 0, 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.board[i][j] = 2
                    val = game.solve(self.board, self.cnt+1, 1)
                    if val > best:
                        best = val
                        x,y = i,j
                    self.board[i][j] = 0
        self.board[x][y] = 2
        return x,y
