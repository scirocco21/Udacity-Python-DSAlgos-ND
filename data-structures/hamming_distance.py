 """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return None
    hamming_dist = len(str1)
    for idx in range(len(str1)):
        if str1[idx] == str2[idx]:
            hamming_dist -= 1
    return hamming_dist