def string_reverser(our_string):
    # in-place solution
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