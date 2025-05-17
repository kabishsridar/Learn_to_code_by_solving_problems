# first get an input from the user for a sentence
sentence = input("enter a sentence(do not use spaces before and after the sentence): ")
# counting the number of words by using count() function with the help of spaces
# number of spaces + 1 will be the number of words
def word_count(words):
    word_count = words.count(' ') + 1
    print("number of words: ",word_count)
word_count(sentence) # calling the function to begin
