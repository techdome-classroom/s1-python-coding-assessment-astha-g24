class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(x: int, y: int) -> None:
            
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 'W':
                return
            
            
            grid[x][y] = 'W'
           
            dfs(x + 1, y)  
            dfs(x - 1, y) 
            dfs(x, y + 1)  
            dfs(x, y - 1) 

        island_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':  
                    island_count += 1   
                    dfs(i, j)           

        return island_count


solution = Solution()

dispatch_1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

dispatch_2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]

dispatch_3=[
    ["W", "W", "W", "W"], 
    ["W", "L", "L", "W"], 
    ["W", "L", "L", "W"], 
    ["W", "W", "W", "W"]
    ]
print(solution.getTotalIsles(dispatch_1))  
print(solution.getTotalIsles(dispatch_2)) 
print(solution.getTotalIsles(dispatch_3))
