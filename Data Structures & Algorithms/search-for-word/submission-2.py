class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(i:int, l:int, r:int):
            if i == len(word):
                return True
            # Check boundaries, character match, and if already visited ('#')
            if (l < 0 or l >= rows or r < 0 or r >= cols or board[l][r] != word[i]):
                return False
            val1, val2, val3,val4 = False, False,False,False
            board[l][r] = "#"
            found = (
                dfs( i + 1, l-1,r) or
                dfs(i + 1,l,r-1) or
                dfs(i + 1, l+1, r) or
                dfs(i+1, l, r+1)
            )
            board[l][r] = word[i]
            return found
        
        for l in range(rows):
            for r in range(cols):
                if(board[l][r] == word[0] and dfs(0, l, r)):
                    return True
        return False