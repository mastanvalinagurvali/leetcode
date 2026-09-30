class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        leftrow=[0]*n
        upperdiagonal=[0]*(2*n-1)
        lowerdiagonal=[0]*(2*n-1)
        def fun(col,board):
            if col==n:
                ans.append([''.join(i) for i in board])
                return 
            for row in range(n):
                if leftrow[row]==0 and lowerdiagonal[row+col]==0 and upperdiagonal[n-1+col-row]==0:
                    board[row][col]="Q"
                    leftrow[row] = 1
                    lowerdiagonal[row + col] = 1
                    upperdiagonal[n - 1 + col - row] = 1

                    fun(col+1,board)
                    board[row][col]='.'
                    leftrow[row] = 0
                    lowerdiagonal[row + col] = 0
                    upperdiagonal[n - 1 + col - row] = 0

        fun(0,[['.']*n for i in range(n)])
        return ans