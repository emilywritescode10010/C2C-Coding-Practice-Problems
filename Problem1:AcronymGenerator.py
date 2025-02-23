# get input by prompting for phrase
phrase = input("Enter the phrase to get an acronym for it: ")

# checks to see if the input is empty or has only whitespace, if true it will keep prompting the user for a valid input
while len(phrase.strip()) == 0:
    print("The string is empty or contains only whitespace.")
    phrase = input("Enter the phrase to get an acronym for it: ")

# converts the phrase to lowercase and creates a list of the words in the phrase by using the split() method
words = phrase.lower().split()

# creates a list of short words that should not be included in the acronym
exluded_words = ["a", "an", "the", "of", "on", "in", "at", "by", "for", "to", "with", "and", "or", "but", "nor"]

# checks to see if the phrase has any of the short words in exluded_words and removes them from the list of words if it does
for word in words:
    if word in exluded_words:
        words.remove(word)

# initializes acronym variable
acronym = ""

# converts the first letter of every word in the list of words to uppercase and adds them to the acronym variable
for word in words:
    acronym += word[0].upper()

# prints the final acronym for the phrase
print(acronym)