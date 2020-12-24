# Write a function that reverses all word in a string while maintaining word order

# helper method
def string_reverser(our_string):
    mid_point = int(len(our_string)/2)
    i = 0
    string_array = list(our_string)
    final_index = len(string_array) - 1
    while i < mid_point:
        temp = string_array[i]
        string_array[i] = string_array[final_index - i]
        string_array[final_index - i] = temp
        i += 1
    separator = ""
    return separator.join(string_array)

def word_flipper(our_string):
    word_array = our_string.split(" ")
    for index,word in enumerate(word_array):
      word_array[index] = string_reverser(word)
    return " ".join(word_array)