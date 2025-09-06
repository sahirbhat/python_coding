list1 = ["word", "backend", "exercise", "frontend", "angular", "php", "matlab"]

class LongestWord:
    def __init__(self, words):
        self.words = words
        self.max_length = 0
        self.longest_word = ""

    def find_longest_word(self):
        for word in self.words:
            if len(word) > self.max_length:
                self.max_length = len(word)
                self.longest_word = word

    def print_longest_word(self):
        print(f"Longest word: '{self.longest_word}' with length {self.max_length}")



s1 = LongestWord(list1)
s1.find_longest_word()
s1.print_longest_word()
