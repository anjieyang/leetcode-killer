class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.node

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        return self.dfs(0, self.node, word)

    def dfs(self, start, root, word):
        curr = root

        for i in range(start, len(word)):
            c = word[i]

            if c == '.':
                for child in curr.children.values():
                    if self.dfs(i + 1, child, word):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
