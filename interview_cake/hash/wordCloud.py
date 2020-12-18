def wordCloud(words):
    wordDict = {}
    wordList = words.split()

    for i in wordList:
        currentWord = i.lower()
        if not currentWord.isalpha():
            currentWord = currentWord[:len(currentWord)-1]
        wordDict[currentWord] = wordDict.get(currentWord, 0) + 1

    return wordDict

def wordCloud2(words):
    print(len(words))
    wordDict = {}
    wordStart = 0
    for i in range(1, len(words)):
        if words[i] == len(words) or not words[i].isalpha():
            currentWord = words[wordStart:i].lower()
            if currentWord.isalpha():
                wordDict[currentWord] = wordDict.get(currentWord, 0) + 1
            wordStart = i + 1
    
    print(wordDict)

# Guided solution
def split_words(input_string):
    words = []
    current_word_start_index = 0
    current_word_length = 0

    for i, char in enumerate(input_string):
        if char.isalpha():
            if current_word_length == 0:
                current_word_start_index = i
            current_word_length += 1
        else:
            word = input_string[current_word_start_index:current_word_start_index + current_word_length]
            words.append(word)
            current_word_length = 0
    
    return words

class WordCloudData:
    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # Iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()
        current_word_start_index = 0
        current_word_length = 0
        for i, character in enumerate(input_string):
            # if we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index: current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
            # If we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == ' ' or character == '\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index: current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0
            # WE want to make sure we split on ellipses so if we get two periods
            # in a row add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string) - 1 and input_string[i + 1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index: current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0
            # If the character is a letter or an apostrophe, we add it to our curren't word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1
            # If the character is a hyphen, we want to check if it's surrounded by letters
            # If it is, we add it to our current word
            elif character == '-':
                if i > 0 and input_string[i-1].isalpha() and input_string[i + 1].isalpha():
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index: current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

    def add_word_to_dictionary(self, word):
        #if the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # If a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's cou
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1
        # If an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]
        # Otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1



def main():
    word = 'After beating the eggs, Dana read the next step:'
    word2 = "We came, we saw, we  cake conquered...then we ate Bill's (Mille-Feuille) cake."
    # print(wordCloud2(word2))
    # print(split_words(word2))
    wordCloud = WordCloudData(word2)
    print(wordCloud.words_to_counts)

main()