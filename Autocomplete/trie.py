class Trie(object):
    def __init__(self):
        self.children = {}
        self.whole_word_flag = False

    def insert(self, word):
        for char in word:
            if char not in self.children:
                self.children[char] = Trie()
            self = self.children[char]
        self.whole_word_flag = True

    def get_suffixes(self, prefix, results = []):
        if self.whole_word_flag:
            results.append(prefix)
        if not self.children: 
            return results
        for (char, node) in self.children.items():
            node.get_suffixes(prefix + char)
        return results
   
    def autocomplete(self, prefix):
        for char in prefix:
            if char not in self.children:
                return []
            self = self.children[char]
        return self.get_suffixes(prefix)


new_trie = Trie()

with open('wordlist.txt', 'r') as rf:
    for line in rf:
        new_trie.insert(line.strip())

word_fragment = input("Enter a word fragment: ")

autocompletion_candidates = new_trie.autocomplete(word_fragment)

for word in autocompletion_candidates:
    print(word)
