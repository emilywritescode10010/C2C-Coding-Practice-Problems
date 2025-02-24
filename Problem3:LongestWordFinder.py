# creates the fuction that will find the longest word given a sentence
def long_word_finder(sentence):
    # if no errors occur it will run this code
    try:
        # creates a list of the words in the sentence by using the split() method
        words = sentence.split()

        # initializes the variable that will hold the same words as the previous list but without punctuation
        new_words = []

        # removes punctuation by going through the words in the list and checking the last character
        for word in words:
            if word[-1] in [",", ".", "!", ":", ";"]:
                word = word[0 : -1]
            new_words.append(word)
        
        # initializes the longest word to be the first word in the list new_words
        longest = new_words[0]

        # goes through the list of words and checks to see if the current word's length is greater than the current longest word's length
        for word in new_words:
            if len(word) > len(longest):
                longest = word
        
        # returns the longest word
        return longest

    # if the user's input is empty or has only whitespace, it handles the error by simply printing a message of what went wrong
    except(IndexError):
        print("The string is empty or contains only whitespace.")

# get input by prompting for sentence
user_sent = input("Enter a sentence: ")

# calls the function that we already defined earlier which will give the longest word of a sentence and prints whatever is returned
print(long_word_finder(user_sent))