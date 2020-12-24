def anagram_checker(str1, str2):
  # clean up input strings by removing spaces and lower casing
    sanitized_str1 = str1.replace(" ", "").lower()
    sanitized_str2 = str2.replace(" ", "").lower()

    if len(sanitized_str1) != len(sanitized_str2):
        return False
    else:
        # break up string into list
        sortable_list1 = list(sanitized_str1)
        sortable_list2 = list(sanitized_str2)
        # sort character array in place
        sortable_list1.sort()
        sortable_list2.sort()
        # check if both arrays are equal as they should be for anagrams
        if sortable_list1 == sortable_list2:
            return True
    return False