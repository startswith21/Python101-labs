# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers"
sentence = word[1:3] + " " + word[9:2:-2] + " " + word[0] + word[-2] + word[2:4] + word[-1]
print(sentence)
