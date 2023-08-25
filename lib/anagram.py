# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([x for x in word])

    def match(self, word_list):
        matches = []

        for word in word_list:
            if sorted([x for x in word]) == self.word_letters:
                matches.append(word)

        return matches

    