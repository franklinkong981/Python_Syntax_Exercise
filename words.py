def print_upper_words(words_list, must_start_with):
    """This function takes in 2 parameters: A list of words called words_list and a set of letters called must_start_with.
       It then prints out the words in words_list that start with one of the letters in must_start_with
       (uppercase or lowercase) in all capital letters."""
    for word in words_list:
        for letter in must_start_with:
            if word[0] == letter.lower() or word[0] == letter.upper():
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})