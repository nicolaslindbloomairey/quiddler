with open("data/words.txt") as f:
    # words.txt is newline delimited. strip newlines and make immutable
    WORDS = tuple([word.strip() for word in f.readlines()])
print(len(WORDS), "words loaded.")
