class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
        

    def addWord(self, word: str) -> None:
        Node=self.root
        for char in word:
            if char not in Node.children:
                Node.children[char]=TrieNode()
            Node=Node.children[char]
        Node.endOfword=True
    

        

    def search(self, word: str) -> bool:
        Node=self.root
        def dfs(j,root):
            curr=root
            for i in range(j,len(word)):
                if word[i] ==".":
                    for node in curr.children.values():
                        if dfs(i+1,node):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                        
                    curr=curr.children[word[i]]
            return curr.endOfword
        return dfs(0,Node)
    
        
