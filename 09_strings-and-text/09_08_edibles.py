# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
dish = s[7:12] + s[26:29] + s[57:63] + s[68] + s[73:76]
print(dish)