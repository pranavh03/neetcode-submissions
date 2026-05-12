class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def search(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= n or c < 0 or c >= m:
                return False
            if board[r][c] != word[i]:
                return False
            if board[r][c] == '#':
                return False

            char = board[r][c]
            board[r][c] = '#'

            res = (
                search(r+1, c, i+1) or
                search(r-1, c, i+1) or
                search(r, c+1, i+1) or
                search(r, c-1, i+1)
            )

            board[r][c] = char
            return res

        for r in range(n):
            for c in range(m):
                if search(r, c, 0):
                    return True
        return False
