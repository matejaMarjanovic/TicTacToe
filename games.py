class TicTacToe:
    def __init__(self):
        self.gameMatrix = [['-' for j in range(3)] for i in range(3)]
        
        self.player = 'x'
        self.winner = '-'
        self.freeFields = 9
    
    def gameEnd(self):
        if self.gameMatrix[0][0] == self.gameMatrix[0][1] == self.gameMatrix[0][2] != '-' or \
            self.gameMatrix[1][0] == self.gameMatrix[1][1] == self.gameMatrix[1][2] != '-' or \
            self.gameMatrix[2][0] == self.gameMatrix[2][1] == self.gameMatrix[2][2] != '-' or \
            self.gameMatrix[0][0] == self.gameMatrix[1][0] == self.gameMatrix[2][0] != '-' or \
            self.gameMatrix[0][1] == self.gameMatrix[1][1] == self.gameMatrix[2][1] != '-' or \
            self.gameMatrix[0][2] == self.gameMatrix[1][2] == self.gameMatrix[2][2] != '-' or \
            self.gameMatrix[0][0] == self.gameMatrix[1][1] == self.gameMatrix[2][2] != '-' or \
            self.gameMatrix[0][2] == self.gameMatrix[1][1] == self.gameMatrix[2][0] != '-':
            self.winner = self.player
            return 1 if self.winner == 'x' else -1
        if self.freeFields == 0:
            return 0
        return None
    
    def play(self, i, j):
        self.gameMatrix[i][j] = self.player
        self.player = 'x' if self.player == 'o' else 'o'
        self.freeFields -= 1
    
    def unplay(self, i, j):
        self.gameMatrix[i][j] = '-'
        self.player = 'x' if self.player == 'o' else 'o'
        self.freeFields += 1
    
    def freeFieldsPositions(self):
        retVal = []
        for i in range(3):
            for j in range(3):
                if self.gameMatrix[i][j] == '-':
                    retVal.append((i, j))
        return retVal
    
    
    def max(self):
        endRes = self.gameEnd()
        if endRes != None:
            return (endRes, None)
        
        currentMax = float('-inf')
        for (i, j) in self.freeFieldsPositions():
            self.play(i, j)
            minValPair = self.min()
            minVal = minValPair[0]
            if minVal > currentMax:
                currentMax = minVal
                bestMove = (i, j)
            self.unplay(i, j)
        return (currentMax, bestMove)
    
    def min(self):
        endRes = self.gameEnd()
        if endRes != None:
            return (endRes, None)
        
        currentMin = float('inf')
        for (i, j) in self.freeFieldsPositions():
            self.play(i, j)
            maxValPair = self.max()
            maxVal = maxValPair[0]
            if maxVal < currentMin:
                currentMin = maxVal
                bestMove = (i, j)
            self.unplay(i, j)
        return (currentMin, bestMove)
    
    def printTable(self):
        for i in range(3):
            for j in range(3):
                print self.gameMatrix[i][j],
            print
    def maxAB(self, alpha, beta):
        endRes = self.gameEnd()
        if endRes != None:
            return (endRes, None)
        
        currentMax = float('-inf')
        for (i, j) in self.freeFieldsPositions():
            self.play(i, j)
            minValPair = self.minAB(alpha, beta)
            minVal = minValPair[0]
            if minVal > currentMax:
                currentMax = minVal
                bestMove = (i, j)
            if currentMax > alpha:
                alpha = currentMax
            if currentMax >= beta:
                self.unplay(i, j)
                return (currentMax, bestMove)
            self.unplay(i, j)
        return (currentMax, bestMove)
    
    def minAB(self, alpha, beta):
        endRes = self.gameEnd()
        if endRes != None:
            return (endRes, None)
        
        currentMin = float('inf')
        for (i, j) in self.freeFieldsPositions():
            self.play(i, j)
            maxValPair = self.maxAB(alpha, beta)
            maxVal = maxValPair[0]
            if maxVal < currentMin:
                currentMin = maxVal
                bestMove = (i, j)
            if currentMin <= alpha:
                self.unplay(i, j)
                return (currentMin, bestMove)
            if currentMin < beta:
                beta = currentMin
            self.unplay(i, j)
        return (currentMin, bestMove)

def main():
    game = TicTacToe()
    finish = None
    while finish == None:
        game.printTable()
        print "Enter the coords for the x and y field you want to put X"
        i = int(raw_input())
        j = int(raw_input())
        while (i, j) not in game.freeFieldsPositions():
            print "Those fields are already taken. Try again"
            i = int(raw_input())
            j = int(raw_input())
        game.play(i, j)
        game.printTable()
        finish = game.gameEnd()
        if finish != None:
            break
        print "----------------"
        print "the computer is playing"
        print "----------------"
        bestMove = game.max()[1]
        game.play(bestMove[0], bestMove[1])
        finish = game.gameEnd()
    
    if finish == 0:
        print("It's a tie")
    elif game.player == 'o':
        print("You won!!!")
    else:
        print("Sorry... the computer won :(")

if __name__ == '__main__':
    main()
