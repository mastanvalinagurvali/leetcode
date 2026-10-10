class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        for i in range(n):
            k=rowShift[i]
            grid[i]=grid[i][k:]+grid[i][:k]
        for j in range(n):
            k=colShift[j]
            col=[]
            for i in range(n):
                col.append(grid[i][j])
            col=col[k:]+col[:k]
            for i in range(n):
                grid[i][j]=col[i]
        return grid