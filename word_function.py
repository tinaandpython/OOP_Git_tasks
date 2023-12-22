# Task 1
# Create a .txt file with several words.
# Create a function that reads the words from the file and returns the longest word from the file:
# The function should take one parameter - the path to the file/file name.
# The function should return - the longest word from the file.
# Get the longest word using the created function. Print the longest word and its length.

def read_file():
    with open("word-function-text", 'r') as words:
        longest_word = max(words, key=len) #  the key=len argument is used to specify that the length of each word should be considered for comparison
        print(longest_word)

read_file()