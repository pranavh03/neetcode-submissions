class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        Node=self.root
        for char in word:
            if char not in Node.children:
                Node.children[char]=TrieNode()
            Node=Node.children[char]
        Node.endOfword=True



    def search(self, word: str) -> bool:
        Node=self.root
        for char in word:
            if char not in Node.children:
                return False
            Node=Node.children[char]
        return Node.endOfword
        

    def startsWith(self, prefix: str) -> bool:
        Node=self.root
        for char in prefix:
            if char not in Node.children:
                return False
            Node=Node.children[char]
        return True
        
        