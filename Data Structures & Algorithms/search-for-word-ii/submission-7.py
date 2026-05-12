class TrieNode():
    def __init__(self):
        self.children={}
        self.endOfword=False
    def addme(self,word:str):
        n=self
        for w in word:
            if w not in n.children:
                n.children[w]=TrieNode()
            n=n.children[w]
        n.endOfword=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows=len(board)
        columns = len(board[0])
        root=TrieNode()
        for word in words:
            root.addme(word)
        visit=set()
        res=set()

        def dfs(r,c,node,word):
            if r<0 or c<0 or r>=rows or c>=columns or (r,c) in visit or board[r][c] not in node.children:
                return 
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.endOfword:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        for r in range(rows):
            for c in range(columns):
                dfs(r,c,root,"")
        return list(res)
            

