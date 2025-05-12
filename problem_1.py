sentence = input("enter a sentence:")
def word_count(words):
    word_count = words.count(' ') + 1
    print("number of words: ",word_count)
word_count(sentence)