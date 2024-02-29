class AbcModel:
    def __init__(self):
        self.used_words = set()

    def is_used(self, word):
        return word in self.used_words

    def add(self, word):
        self.used_words.add(word)