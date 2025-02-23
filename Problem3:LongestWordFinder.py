def long_word_finder(sentence):
    
    try:
        words = sentence.split()

        new_words = []

        for word in words:
            if word[-1] in [",", ".", "!", ":", ";"]:
                word = word[0 : -1]
            new_words.append(word)
        
        longest = new_words[0]

        for word in new_words:
            if len(word) > len(longest):
                longest = word

        return longest

    except(IndexError):
        print("The string is empty or contains only whitespace.")


user_sent = input("Enter a sentence: ")

print(long_word_finder(user_sent))