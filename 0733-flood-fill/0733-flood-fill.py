class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        r, c = len(image), len(image[0])
        def dfs(row, col):
            if not (0<=row<r and 0<=col<c):
                return
            if image[row][col]==oldColor:
                image[row][col] = color
                dfs(row, col-1)
                dfs(row, col+1)
                dfs(row-1, col)
                dfs(row+1, col)
        if(oldColor != color):
            dfs(sr, sc)
        return image