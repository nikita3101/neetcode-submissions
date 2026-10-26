class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        queue = deque()
        def bfs(i: int, j :int):
            queue.append([i,j])
            while len(queue)>0:
                cell = queue.pop()
                #print(cell[0])
                #print(cell[1])
                grid[cell[0]][cell[1]] = "-1"
                if cell[0] + 1 <len(grid) and grid[cell[0]+1][cell[1]] == "1":
                    queue.append([cell[0] + 1, cell[1]])
                if cell[0] - 1 >= 0 and grid[cell[0]-1][cell[1]] == "1":
                    queue.append([cell[0] - 1, cell[1]])
                if cell[1] + 1 <len(grid[0]) and grid[cell[0]][cell[1]+1] == "1":
                    queue.append([cell[0], cell[1]+1])
                if cell[1] - 1 >= 0 and grid[cell[0]][cell[1]-1] == "1":
                    queue.append([cell[0], cell[1]-1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]=="1"):
                    count = count +1
                    bfs(i, j)
        return count

